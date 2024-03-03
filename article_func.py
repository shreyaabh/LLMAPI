
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate
import os
import random
import openai
from langchain.chat_models import ChatOpenAI
import time
from langchain.chains import LLMChain

def article_generator(topic, key_word, language):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo-1106",
        openai_api_key='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',
        temperature=0,
        max_tokens=4095
    )
    
    prompt_template ="""Role: Act as a content writer. You are about to write an article for an edtech site. 
        Task: Generate an article for the requested topic. Generate the output as shown in the example below: 

        Example : 

        Input Query : Generate me an article for "Least Common Multiple"

        OUTPUT:

        Title
        Understanding the Concept of Least Common Multiple (LCM)

        Introduction

        <h3>What is LCM?:</h3>
        When dealing with numbers, especially in mathematics, you often come across the term "Least Common Multiple" or LCM. But what exactly does it mean? Let's dive into the world of LCM and understand its significance in solving mathematical problems.

        Definition

        <h3>The LCM Explained: </h3>
        The Least Common Multiple (LCM) of two or more numbers is the smallest multiple that is exactly divisible by each of the numbers. In simpler terms, it is the smallest number that is a multiple of all the given numbers.

        Methods

        <h3>Finding the LCM: </h3>
        There are various methods to find the LCM of numbers. One common method is to list the multiples of each number and find the smallest multiple that is common to all the numbers. Another method involves using prime factorization to find the LCM.

        Example

        <h3>Finding the LCM of 12 and 15:</h3>
        <strong> Step 1: </strong> List the multiples of each number
        Multiples of 12: 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, ...
        Multiples of 15: 15, 30, 45, 60, 75, 90, 105, 120, ...
        <strong> Step 2: </strong> Identify the smallest common multiple
        The smallest common multiple of 12 and 15 is 60.
        So, the LCM of 12 and 15 is 60.

        Quizzes

        <strong>1. "The Bakery Dilemma"</strong>
        <strong> Scenario: </strong>
        A bakery needs to pack cookies in boxes of 12 and 15. What is the least number of cookies they can pack in each box to ensure no cookies are left over?
        A) 60 cookies
        B) 30 cookies
        C) 45 cookies
        D) 120 cookies
        Equation: LCM of 12 and 15
        Answer: A) 60 cookies

        <strong>2. "The Garden Planting Puzzle"</strong>
        <strong> Scenario: </strong> A gardener wants to plant flowers in rows of 8 and 10. What is the least number of flowers they need to plant to fill each row without any flowers left over?
        A) 40 flowers
        B) 80 flowers
        C) 20 flowers
        D) 100 flowers
        Equation: LCM of 8 and 10
        Answer: A) 40 flowers

        <strong>3. "The Classroom Seating Arrangement"</strong>
        <strong> Scenario: </strong> A teacher wants to arrange students in rows of 6 and 9. What is the least number of students needed to fill each row without any students left over?
        A) 18 students
        B) 36 students
        C) 12 students
        D) 24 students
        Equation: LCM of 6 and 9
        Answer: A) 18 students

        <strong>4. "The Music Playlist Dilemma"</strong>
        <strong> Scenario: </strong> A DJ wants to create a playlist with songs that repeat every 4 and 6 minutes. What is the least amount of time before the playlist repeats a song?
        A) 12 minutes
        B) 24 minutes
        C) 18 minutes
        D) 36 minutes
        Equation: LCM of 4 and 6
        Answer: A) 12 minutes

        <strong>5. "The Sports Equipment Packing Challenge"</strong>
        <strong>Scenario: </strong>A coach needs to pack sports equipment in bags of 5 and 7. What is the least number of equipment items they can pack in each bag without any items left over?
        A) 35 items
        B) 70 items
        C) 25 items
        D) 50 items
        Equation: LCM of 5 and 7
        Answer: A) 35 items

        Tips and Tricks

        <strong>1. The Bakery Dilemma</strong>
        <strong>Scenario:</strong> Finding the LCM of 12 and 15.
        <strong>Tip: </strong>To find the LCM, list the multiples of each number and identify the smallest common multiple.
        Calculation: Multiples of 12: 12, 24, 36, 48, 60, ...
        Multiples of 15: 15, 30, 45, 60, ...
        Smallest common multiple: 60
        Answer: A) 60 cookies.

        <strong>2. The Garden Planting Puzzle</strong>
        <strong>Scenario:</strong> Finding the LCM of 8 and 10.
        <strong>Tip: </strong>List the multiples of each number and identify the smallest common multiple to find the LCM.
        Calculation: Multiples of 8: 8, 16, 24, 32, 40, ...
        Multiples of 10: 10, 20, 30, 40, ...
        Smallest common multiple: 40
        Answer: A) 40 flowers.

        <strong>3. The Classroom Seating Arrangement</strong>
        <strong>Scenario:</strong> Finding the LCM of 6 and 9.
        <strong>Tip:</strong> Use the method of listing multiples to find the LCM of the given numbers.
        Calculation: Multiples of 6: 6, 12, 18, 24, 30, ...
        Multiples of 9: 9, 18, 27, 36, ...
        Smallest common multiple: 18
        Answer: A) 18 students.

        <strong>4. The Music Playlist Dilemma</strong>
        <strong>Scenario:</strong> Finding the LCM of 4 and 6.
        <strong>Tip:</strong> List the multiples of each number and identify the smallest common multiple to find the LCM.
        Calculation: Multiples of 4: 4, 8, 12, 16, 20, ...
        Multiples of 6: 6, 12, 18, 24, ...
        Smallest common multiple: 12
        Answer: A) 12 minutes.

        <strong>5. The Sports Equipment Packing Challenge</strong>
        <strong>Scenario:</strong> Finding the LCM of 5 and 7.
        <strong>Tip:</strong> Use the method of listing multiples to find the LCM of the given numbers.
        Calculation: Multiples of 5: 5, 10, 15, 20, 25, ...
        Multiples of 7: 7, 14, 21, 28, ...
        Smallest common multiple: 35
        Answer: A) 35 items.

        Real-Life Applications

        <strong>Story: "The LCM Adventure of Alex and Lily"</strong>
        Alex and Lily were two adventurous siblings who loved solving puzzles and riddles. One day, they encountered a series of challenges that required them to use the concept of LCM to overcome obstacles and complete their quests.

        <strong>Challenge 1: The Treasure Hunt</strong>
        Alex and Lily embarked on a treasure hunt that led them to a mysterious cave. Inside the cave, they found a locked chest with a riddle written on it. The riddle stated, "To open the chest, find the least number that is a multiple of 4, 6, and 8." Remembering their lessons on LCM, Alex and Lily quickly calculated the LCM of 4, 6, and 8, which turned out to be 24. They used the number to unlock the chest and discovered a map to the hidden treasure.

        <strong>Challenge 2: The Magical Bridge</strong>
        As they continued their adventure, Alex and Lily encountered a magical bridge guarded by a mystical creature. The creature challenged them to find the least number of steps that would cause the bridge to light up. The steps were numbered 5, 7, and 9. Applying their knowledge of LCM, Alex and Lily calculated the LCM of 5, 7, and 9, which turned out to be 315. As they took 315 steps, the bridge lit up, allowing them to cross safely.

        <strong>Challenge 3: The Enchanted Garden</strong>
        In the final challenge, Alex and Lily entered an enchanted garden filled with beautiful flowers. They were tasked with arranging the flowers in rows, with each row containing 12, 15, and 18 flowers. Using the concept of LCM, they determined that they needed 180 flowers to fill each row without any flowers left over. The garden bloomed with vibrant colors, and the siblings completed their adventure successfully.

        FAQ

        Q.1
        What is the significance of finding the LCM of numbers?
        A: Finding the LCM is important in various mathematical and real-life scenarios. It helps in solving problems related to scheduling, repeating patterns, and resource allocation. In mathematics, the LCM is used in operations involving fractions, simplifying expressions, and solving equations.

        Q.2
        How is the LCM related to the concept of multiples?
        A: The LCM is directly related to the concept of multiples. It represents the smallest common multiple of two or more numbers. Multiples are the result of multiplying a number by an integer, and the LCM is the smallest multiple that is common to all the given numbers.

        Q.3
        Can the LCM be used to find the common denominator in fractions?
        A: Yes, the LCM is used to find the common denominator when adding or subtracting fractions. By finding the LCM of the denominators, you can convert the fractions to equivalent fractions with the same denominator, making it easier to perform operations.

        Q.4
        Are there specific methods to find the LCM of numbers?
        A: Yes, there are different methods to find the LCM, including listing multiples, using prime factorization, and using the method of division. Each method has its advantages and can be applied based on the given numbers and the preferred approach.

        Q.5
        How does the concept of LCM apply to real-life situations?
        A: The concept of LCM has practical applications in various real-life situations, such as scheduling events, planning recurring tasks, and organizing resources. It helps in determining the least amount of time, distance, or quantity needed to fulfill specific requirements, making it a valuable tool in problem-solving.


        Instruction: 
        1. Always include Title, Introduction, Defination, Methods, Example, Quizzes, Real-Life Applications and FAQs.
        2. Always put the h3 tag between each sub heading and strong tag between each context . For eg: "<h3>sub heading</h3>, <strong>context</strong>.
        3. Always compulsorily generate 5 Examples, 5 Tips and Tricks, 5 Quizzes,5 Real-Life Applications and 5 FAQs. More than one 'tips and tricks', 'Real-Life Applications' and 'quizzes' can be added for each keywords to make 5 in total for all three categories.
        4. Always generate article of around 5000-6000 words.
        5. Do not add a conclusion. Finish at FAQ.


        {context}
        """

    prompt = PromptTemplate(
            input_variables=["context"],
            template=prompt_template,)
    
    chain = LLMChain(llm=llm, prompt= prompt)
    
    query = f'''Generate me an article for "{topic}" in language "{language}". Compulsorily use these keywords in article : "{key_word}".'''

    content = chain.run(query)
    print(content)
    
    return content 