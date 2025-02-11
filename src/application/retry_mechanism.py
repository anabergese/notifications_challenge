import asyncio
import logging
from typing import Any, Callable, Coroutine, Type, TypeVar, Union

T = TypeVar("T")


async def retry_with_backoff(
    func: Callable[..., Coroutine[Any, Any, T]],
    args: tuple = (),
    exceptions: Union[Type[BaseException], tuple[Type[BaseException], ...]] = (
        Exception,
    ),
    max_retries: int = 5,
    backoff_strategy: Callable[[int], int] = lambda attempt: attempt * 2,
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
                logging.error("Max retries reached for %s:", exc)
                raise
        except Exception as unexpected_error:
            logging.error(
                "Unexpected error in function %s: %s",
                getattr(func, "__name__", "<unknown>"),
                unexpected_error,
            )
            raise
