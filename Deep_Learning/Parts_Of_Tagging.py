import nltk
nltk.download('averaged_perceptron_tagger_eng')
corpos="""R Ummadivaram is blessed with a stunning natural environment
that captivates visitors with its simplicity and charm. The village is 
surrounded by expansive agricultural lands, which bloom with crops 
throughout the year, showcasing the hard work of its farmers. The rolling
hills and lush forests in the vicinity add to the landscape’s beauty, 
providing a serene backdrop for anyone seeking tranquility in nature. 
The peaceful ambiance is complemented by the clear skies and the gentle 
rustling of leaves, creating a perfect setting for relaxation."""
sensentences=nltk.sent_tokenize(corpos)
print(f"the sensesncs is =>{sensentences}")
#parts od sppech tagging
for i in range(len(sensentences)):
    words=nltk.word_tokenize(sensentences[i])
    #words=[word for word in words if word not in set(nltk.sto)]
    parts=nltk.pos_tag(words)
    print(f"the parts of speech tagging{parts}")
    