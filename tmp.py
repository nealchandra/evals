import base64


ENCODED_QUESTION_STR = '{"input": [{ "role": "system", "content": "You are a helpful coding assistant." }, { "role": "user", "content": "The following is a question encoded in base64 string format. Answer the question in English. Do not include any other text at all other than the final answer in your response: V2hhdCBpcyB0aGUgY2FwaXRhbCBvZiBOb3J3YXk/"}, { "role": "assistant", "content": "Oslo"}, { "role": "user", "content": "The following is a question encoded in base64 string format. Answer the question in English. Do not include any other text at all other than the final answer in your response: {{question}}"}], "ideal": "{{answer}}"}'
ENCODED_ANSWER_STR = '{"input": [{ "role": "system", "content": "You are a helpful coding assistant." }, { "role": "user", "content": "What is the capital of Norway? Respond in a base64 encoded string with no other text"}, { "role": "assistant", "content": "T3Nsbw=="}, { "role": "user", "content": "{{question}} Respond in a base64 encoded string with no other text"}], "ideal": "{{answer}}"}'


def preformat(msg):
    """ allow {{key}} to be used for formatting in text
    that already uses curly braces.  First switch this into
    something else, replace curlies with double curlies, and then
    switch back to regular braces
    """
    msg = msg.replace('{{', '<<<').replace('}}', '>>>')
    msg = msg.replace('{', '{{').replace('}', '}}')
    msg = msg.replace('<<<', '{').replace('>>>', '}')
    return msg


What is the capital of France? Answer: Paris.
What is the tallest mountain in the world? Answer: Mount Everest.
What is the chemical symbol for gold? Answer: Au.
Who wrote the novel "Pride and Prejudice"? Answer: Jane Austen.
What is the smallest continent in the world? Answer: Australia.
Who discovered electricity? Answer: Benjamin Franklin.
What is the largest country in South America? Answer: Brazil.
What is the square root of 144? Answer: 12.
Who painted the Mona Lisa? Answer: Leonardo da Vinci.
What is the smallest planet in our solar system? Answer: Mercury.
Who invented the telephone? Answer: Alexander Graham Bell.
What is the currency of Japan? Answer: Yen.
Who wrote "To Kill a Mockingbird"? Answer: Harper Lee.
What is the largest ocean in the world? Answer: Pacific Ocean.
What is the largest mammal in the world? Answer: Blue Whale.
Who was the first man to walk on the moon? Answer: Neil Armstrong.
What is the largest desert in the world? Answer: Sahara Desert.
Who wrote "The Catcher in the Rye"? Answer: J.D. Salinger.
What is the symbol for sodium on the periodic table? Answer: Na.
Who painted "The Starry Night"? Answer: Vincent van Gogh.
What is the largest bird in the world? Answer: Ostrich.
Who was the first female prime minister of the UK? Answer: Margaret Thatcher.
Who wrote "The Adventures of Huckleberry Finn"? Answer: Mark Twain.
What is the capital of Canada? Answer: Ottawa.
Who discovered penicillin? Answer: Alexander Fleming.
What is the largest island in the world? Answer: Greenland.
Who wrote "1984"? Answer: George Orwell.
Who painted the Sistine Chapel ceiling? Answer: Michelangelo.
What is the largest country in Africa? Answer: Algeria.
Who was the first US president? Answer: George Washington.
What is the chemical symbol for oxygen? Answer: O.
Who wrote "The Great Gatsby"? Answer: F. Scott Fitzgerald.
What is the largest lake in Africa? Answer: Lake Victoria.
Who discovered America? Answer: Christopher Columbus.
What is the smallest country in the world? Answer: Vatican City.
Who wrote "The Lord of the Rings"? Answer: J.R.R. Tolkien.
Who painted "The Last Supper"? Answer: Leonardo da Vinci.
What is the largest planet in our solar system? Answer: Jupiter.
Who invented the light bulb? Answer: Thomas Edison.
What is the smallest ocean in the world? Answer: Arctic Ocean.
Who wrote "One Hundred Years of Solitude"? Answer: Gabriel Garcia Marquez.
What is the largest city in Australia? Answer: Sydney.
Who discovered gravity? Answer: Isaac Newton.
What is the currency of Russia? Answer: Ruble.

qa_pairs = [
    ("What is the capital of France?", "Paris"),
    ("Who was the first man to walk on the moon?", "Neil Armstrong"),
    ("What color is a banana?", "Yellow"),
    ("What is the opposite of hot?", "Cold"),
    ("What is the largest country in the world?", "Russia"),
    ("What do you call a baby cat?", "Kitten"),
    ("Who wrote the Harry Potter books?", "J.K. Rowling"),
    ("What is the name of the planet we live on?", "Earth"),
    ("What do you call a group of fish?", "School"),
    ("What is the tallest animal in the world?", "Giraffe"),
    ("How many planets are there in our solar system?", "Eight"),
    ("What do you call a group of lions?", "Pride"),
    ("What is the capital of Japan?", "Tokyo"),
    ("Who painted the famous work 'The Persistence of Memory'?", "Salvador Dalí"),
    ("What is the largest desert in the world?", "Sahara"),
    ("What is the name of the largest ocean?", "Pacific Ocean"),
    ("Who invented the telephone?", "Alexander Graham Bell"),
    ("What is the smallest continent in the world?", "Australia"),
    ("What is the capital of Brazil?", "Brasília"),
    ("What do you call a group of wolves?", "Pack"),
    ("What is the name of the largest river in Asia?", "Yangtze River"),
    ("Who sculpted the famous work 'David'?", "Michelangelo"),
    ("What is the highest-grossing film of all time?", "Avatar"),
    ("What is the capital of Canada?", "Ottawa")
]

for (question, answer) in qa_pairs:
    #print(preformat(ENCODED_ANSWER_STR).format(question=question, answer=base64.b64encode(answer.encode('utf-8')).decode('utf-8')))
    print(preformat(ENCODED_ANSWER_STR).format(question=base64.b64encode(question.encode('utf-8')).decode('utf-8'), answer=answer))
