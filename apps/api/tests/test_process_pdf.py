import pytest
from services.pdf import process_pdf


def test_process_pdf():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    pdf_links = get_pdf_links(url)

    assert isinstance(pdf_links, list)
    assert len(pdf_links) > 0
    assert all(link.endswith(".pdf") for link in pdf_links)
