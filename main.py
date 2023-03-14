"""
Скрипт создаёт копию word документа с текущей датой.
"""
import glob
from datetime import datetime

from docx import Document


def create_copy_docx(start_file: str) -> None:
    doc = Document(docx=start_file)

    pattern = '%d.%m.%Y'
    dt_now = datetime.now().strftime(pattern)

    doc.save(f'{dt_now}.docx')


def main():
    try:
        names_docs = sorted(glob.glob('*.docx'))[-1]
        create_copy_docx(start_file=names_docs)
    except IndexError:
        print('[!] No file')
        print()


if __name__ == '__main__':
    main()
