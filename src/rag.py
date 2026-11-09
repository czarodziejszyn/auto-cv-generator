from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_vector_store(data_dir: str, persist_dir: str = "./chroma_db"):
    # 1. Załaduj pliki markdown z data_dir
    loader = DirectoryLoader(data_dir)
    md_texts = loader.load()
    # 2. Podziel tekst za pomocą text splittera
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.create_documents(md_texts)
    # 3. Zainicjalizuj HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # 4. Zbuduj i zapisz bazę Chroma (metoda .from_documents)
    Chroma.from_documents(
        documents=documents, embeddings=embeddings, persist_directory=persist_dir
    )


def get_retriever(persist_dir: str = "./chroma_db"):
    # 1. Załaduj istniejącą bazę Chroma z dysku
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(
        persist_directory=persist_dir, embeddings=embeddings
    )
    # 2. Zwróć obiekt retrievera (baza.as_retriever())
    return vector_store.as_retriever()
