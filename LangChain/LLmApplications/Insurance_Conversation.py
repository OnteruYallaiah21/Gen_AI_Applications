from langchain_core.prompts import PromptTemplate 
insurance_conversation = [
    {
        "customer": "What types of insurance do you offer?",
        "chatbot": "We offer a variety of insurance options, including health, life, auto, home, and travel insurance. Would you like more information on a specific type?"
    },
    {
        "customer": "Can you explain the benefits of health insurance?",
        "chatbot": "Health insurance provides coverage for medical expenses, including doctor's visits, hospital stays, and surgeries. It helps protect you from high healthcare costs."
    },
    {
        "customer": "How can I file a claim for my auto insurance?",
        "chatbot": "To file a claim, you can call our claims department at 1-800-555-1234 or visit our website to submit a claim online. Make sure to have your policy number handy."
    },
    {
        "customer": "What factors affect my life insurance premium?",
        "chatbot": "Your life insurance premium can be affected by several factors, including your age, health history, lifestyle choices, and the coverage amount you select."
    },
    {
        "customer": "Do you provide coverage for pre-existing conditions?",
        "chatbot": "Coverage for pre-existing conditions varies by policy. Please provide more details about your situation, and I can help you find the best coverage options."
    },
    {
        "customer": "What is the process to cancel my policy?",
        "chatbot": "To cancel your policy, please contact our customer service at 1-800-555-6789. They will guide you through the cancellation process and any necessary paperwork."
    },
    {
        "customer": "Are there any discounts available for bundling policies?",
        "chatbot": "Yes, we offer discounts for bundling multiple policies, such as home and auto insurance. Please let us know which policies you are interested in, and we can provide a quote."
    },
    {
        "customer": "How do I update my personal information?",
        "chatbot": "You can update your personal information by logging into your online account or by calling our customer service team. They will assist you with the updates."
    },
    {
        "customer": "What should I do if I have an emergency?",
        "chatbot": "In case of an emergency, please call 911 for immediate assistance. After that, you can contact our claims department to report any damages or losses."
    },
    {
        "customer": "Can you help me understand the terms of my policy?",
        "chatbot": "Of course! Please provide your policy number, and I can explain the key terms and coverage details specific to your policy."
    }
]
fprmatingTemplate=PromptTemplate.from_template("Customer:{customer}\nChatBot{chatbot}")

for con in insurance_conversation:
    print("I want the help regarding to know better about the Insurance ")
    print(fprmatingTemplate.invoke(con).to_string())
    
