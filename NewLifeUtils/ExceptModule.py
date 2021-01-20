import traceback

from NewLifeUtils.FileModule import create_files, get_yaml
from NewLifeUtils.LoggerModule import err, log, wrn
from NewLifeUtils.StringUtilModule import screate

default_lang = """
type: "Type"
unknown: "Unknown Error"
about: "More information"
attention: "Attention"
info: "Info"
warning: "Warn"
error: "Error"
fatal: "Fatal error"
wrong: "Something wrong..."

"""
create_files("except_translation", "lang.yml", "exceptsettings", default_lang)
translation = get_yaml("except_translation", default_lang)


def except_print(exception, exceptionType="err", tb=True):
    errorText = "\n-------------- {ExceptionTitle} --------------------\n"
    errorText += f"{translation['type']}: {type(exception).__name__}\n\n"

    if exception.args == 0:
        errorText += f'{translation["unknown"]}\n'
    else:
        errorText += f'{translation["about"]}:\n\t{(chr(10) + chr(9)).join(exception.args)}\t\n'

    if tb:
        errorText += f"\n{traceback.format_exc()}"

    errorText += "\n-------------- {ExceptionTitle} --------------------\n"

    if exceptionType == "attention":
        log(
            errorText.replace(
                "{ExceptionTitle}",
                screate(translation['attention'], 20),
            )
        )
    if exceptionType == "wrn":
        wrn(
            errorText.replace(
                "{ExceptionTitle}",
                screate(translation['warning'], 20),
            )
        )
    elif exceptionType == "err":
        err(
            errorText.replace(
                "{ExceptionTitle}",
                screate(translation['error'], 20),
            )
        )
    elif exceptionType == "fatal":
        err(
            errorText.replace(
                "{ExceptionTitle}",
                screate(translation['fatal'], 20),
            )
        )
        exit(-1)
    else:
        err(
            errorText.replace(
                "{ExceptionTitle}",
                screate(translation['wrong'], 20),
            )
        )


def get_etypes(self):
    return ['attention', 'wrn', 'err', 'fatal']