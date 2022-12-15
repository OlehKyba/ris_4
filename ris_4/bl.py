import logging

log = logging.getLogger(__name__)


def decrease_by_one_letter(word: str) -> str:
    if not word:
        log.warning(
            f'[RIS-4] Can not decrease empty string: {word=}'
        )
        return word

    return word[:-1]
