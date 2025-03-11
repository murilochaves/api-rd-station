from setuptools import setup, find_packages

setup(
    name="api-rd-station",  # Nome do pacote no PyPI
    version="0.1.0",  # Versão inicial
    author="Murilo Chaves Jayme",
    author_email="",
    description="Biblioteca para facilitar a integração com a API do RD Station CRM",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/murilochaves/api-rd-station",
    packages=find_packages(),  # Encontra automaticamente os pacotes no projeto
    install_requires=[
        "requests",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
