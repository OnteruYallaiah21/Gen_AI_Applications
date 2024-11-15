import nltk

sensetesnes="""R Ummadivaram is blessed with a stunning natural environment
that captivates visitors with its simplicity and charm. The village is 
surrounded by expansive agricultural lands, which bloom with crops 
throughout the year, showcasing the hard work of its farmers. The rolling
hills and lush forests in the vicinity add to the landscape’s beauty, 
providing a serene backdrop for anyone seeking tranquility in nature. 
The peaceful ambiance is complemented by the clear skies and the gentle 
rustling of leaves, creating a perfect setting for relaxation."""

words=nltk.word_tokenize(sensetesnes)
pos_Tagged=nltk.pos_tag(words)
named=nltk.ne_chunk(pos_Tagged)
print(f"Named Entity Reconization{named.draw()}")