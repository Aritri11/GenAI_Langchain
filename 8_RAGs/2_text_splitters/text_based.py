from langchain_text_splitters import RecursiveCharacterTextSplitter

text='''Science is the whisper of the universe,
The quiet question that never sleeps,
The spark in the mind of a curious child,
The promise a bold explorer keeps.

It lives in the fall of an apple from a tree,
In the orbit of planets far away,
In the dance of atoms, unseen yet real,
In the night that turns to day.

Science is the language of the stars,
Written in numbers, logic, and light,
Decoding the age of mountains and seas,
Measuring darkness, defining bright.

It asks not for belief but for wonder,
Not for faith but a reasoned view,
It builds its throne on evidence strong,
Where ideas are tested and born anew.'''

splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)

chunks=splitter.split_text(text)

print(len(chunks))
print(chunks)