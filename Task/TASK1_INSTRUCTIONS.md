Task 1: AI-Powered Debugging and Refactoring


Scenario
You're a Graduate Developer at Datacom. A client has reported that a critical nightly data processing script, process_data.py, is failing intermittently and running significantly slower than its service-level agreement (SLA) allows. The original developer has since moved to a different team, and the code is poorly documented. Your manager has tasked you with investigating the script, fixing the bug, and optimising its performance as a top priority. You will submit your work in one file. However, the example answer in the next step will show each piece separately. You will need to partner closely with your AI co-pilot to successfully navigate this challenge.


Step 1: Understand the Codebase

Open the provided process_data.py file in your AI-powered IDE.
The first step in tackling any unfamiliar code is to build a mental model of its purpose. Select the entire content of the file.
Using your IDE's conversational chat feature, submit the following prompt: This is a legacy Python script. Please provide a high-level summary of what it's supposed to do. Then, break down your explanation function by function, detailing the purpose of each, its expected inputs and outputs, and any side effects. Finally, identify any potential areas of concern or parts of the code that seem overly complex or inefficient.


Step 2: Diagnose the Specific Bug

You have been provided with a sample error log file, error.log.
In the AI chat, provide the relevant code snippet from the function that failed and the full content of the error log. Use a prompt structured for diagnosis: Given the following function from the script and the associated error log, what is the most likely root cause of the failure? Please explain your reasoning step-by-step, referencing specific lines of code and the error message.


Step 3: Write a Test to Replicate the Bug

A core principle of professional software development is to never apply a fix without first having a test that reliably reproduces the bug.
Ask your AI partner to help you create this test: Based on your analysis of the bug, write a Python unit test using the 'unittest' library that is specifically designed to fail in the same way the error log shows. This test should call the problematic function with data that triggers the bug.
Save the generated code into a new file named TEST_CASES.py. Run this test from your terminal to confirm that it fails as expected.


Step 4: Refactor and Fix the Code

With a failing test in place, you can now confidently fix the bug. Select the problematic function within process_data.py.
Give a targeted instruction to your AI, such as: Refactor this function to fix the bug we identified. While doing so, also improve its performance. The current implementation uses inefficient nested for-loops; please replace this logic with a more performant method, such as using a dictionary lookup.
After the AI applies the changes, run your unit test suite from TEST_CASES.py again. It should now pass.


Step 5: Document Your Work

Throughout this process, maintain your DEBUG_LOG.md file. For each major step, copy your most important prompts and the most helpful parts of the AI's responses into this file. Add your own brief notes explaining your thought process.

 

