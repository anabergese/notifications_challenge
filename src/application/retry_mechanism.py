import asyncio
import logging
from typing import Any, Callable, Coroutine, Type, TypeVar, Union

T = TypeVar("T")


async def retry_with_backoff(
    *args,
    func: Callable[..., Coroutine[Any, Any, T]],
    exceptions: Union[Type[BaseException], tuple[Type[BaseException], ...]],
    max_retries: int = 3,
    backoff_strategy: Callable[[int], int] = lambda attempt: 2**attempt,
    **kwargs,
) -> T:
    for attempt in range(1, max_retries + 1):
        try:
            return await func(*args, **kwargs)
        except exceptions as exc:
            if attempt < max_retries:
                logging.warning(
                    "Attempt %d/%d failed with error: %s. Retrying...",
                    attempt,
                    max_retries,
                    exc,
                )
                await asyncio.sleep(backoff_strategy(attempt))
            else:
                logging.error(
                    "Max retries reached for function %s: %s", func.__name__, exc
                )
                raise
        except Exception as unexpected_error:
            logging.critical(
                "Unexpected error in function %s: %s", func.__name__, unexpected_error
            )
            raise
