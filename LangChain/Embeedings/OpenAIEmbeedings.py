import os 
from langchain.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
 # Import the Document class

set_llm_cache(InMemoryCache())
apikey=os.getenv('OPEN_AI_KEY_P')
try:
    OPENAI_API_KEY=apikey
    embeedings=OpenAIEmbeddings(model='text-embedding-3-large',api_key=apikey)
    document_content = """
Yes, prolonged sitting can lead to pain in your right buttock (or elsewhere), commonly caused by pressure on the muscles, nerves, or joints. Some possible reasons for the discomfort include:

1. Piriformis Syndrome:
The piriformis muscle in the buttock can irritate or compress the sciatic nerve, leading to pain.
Symptoms: Pain or tingling in the buttock, sometimes radiating down the leg.
2. Ischial Bursitis:
Inflammation of the bursa near the ischial tuberosity (sitting bone) from prolonged sitting or pressure.
Symptoms: Tenderness or pain localized to the sitting area.
3. Sciatica:
Pressure on the sciatic nerve due to posture or underlying issues like a herniated disc.
Symptoms: Pain radiating from the buttock down the leg.
4. Muscle Strain or Imbalance:
Sitting for long hours can lead to tightness in the gluteal or hip flexor muscles, causing discomfort.
5. Poor Posture:
Incorrect sitting posture can place undue stress on the pelvis and lower back.
6. Hard or Unsupportive Chair:
Chairs without proper padding or ergonomic support can cause pressure points.
Steps to Relieve and Prevent Pain:
Adjust Your Chair:

Use an ergonomic chair with lumbar support.
Ensure your hips are slightly higher than your knees.
Take Breaks:

Stand and stretch every 30–60 minutes.
Walk around to improve blood circulation.
Stretch and Strengthen:

Perform stretches like:
Piriformis stretch.
Hamstring and glute stretches.
Strengthen your core and glutes to support your posture.
Use a Cushion:

Consider a coccyx or orthopedic seat cushion to reduce pressure.
Check Your Posture:

Keep your feet flat on the ground.
Maintain a neutral spine alignment.
Apply Heat or Ice:

Ice for acute pain or inflammation.
Heat to relax tight muscles.
If the pain persists or worsens, it’s a good idea to consult a healthcare provider for a thorough evaluation. They can help identify any underlying conditions and recommend tailored treatments.    """
    # Convert the string into a Document object
    document = Document(page_content=document_content)
    spilitng_Text=RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    docSplit=spilitng_Text.split_documents([document])
    db=Chroma.from_documents(docSplit,embeedings)
    query_Results=db.similarity_search('Affordable')
    print(f'the embeeding is Query is=> {query_Results}')
    #storing the vector store in Chroma db
    for result in query_Results:
        print(f"the simi;larity search results content is \n=>{result.page_content}")
    
except Exception as e:
    print(f"the exception is {e}")



