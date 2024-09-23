# 📧 NextGen AI - Cold Email Generator

This Cold Email Generator project is designed for service companies to streamline their business outreach efforts. Using the powerful combination of **Llama 3.1 LLM**, **Groq**, **LangChain**, **Streamlit**, and **ChromaDB**, the tool extracts job listings from company career pages and generates personalized cold emails tailored to the specific job descriptions.

## Overview

The Cold Email Generator enables users to input the URL of a company's careers page. It automatically extracts job listings from the page and, using advanced natural language processing, generates customized cold emails aimed at the company’s hiring team. The generated emails include portfolio links pulled from a vector database, helping service companies pitch their solutions or services with precision and personalization.

### Tech Stack

- **Llama 3.1 LLM**: Generates high-quality and context-aware email content.
- **Groq**: Provides fast and scalable AI acceleration, optimizing LLM performance.
- **LangChain**: Enables seamless integration of language models and structured data.
- **Streamlit**: A user-friendly interface for inputting career page URLs and generating emails.
- **ChromaDB**: A vector database for storing and retrieving portfolio links based on job descriptions.

## Features

- **Career Page Parsing**: Extract job listings from the URL of any company’s careers page.
- **Cold Email Generation**: Create personalized emails for business outreach, highlighting specific service offerings and expertise.
- **Portfolio Suggestions**: Automatically include portfolio links that match the job descriptions, sourced from a vector database.
- **Easy-to-Use Interface**: Built on Streamlit for quick and simple interaction.

## Input Scenario Example

For example, if Meta (Facebook) needs a Software Engineer, iOS, the business development executive (Max) from "XYZ Company (meta 2)" — a Software Development company — can use this tool to craft a personalized cold email. The tool will extract the relevant job listing from Meta's careers page, and generate an email outlining how XYZ Company can assist in meeting Meta's hiring needs.

### Input

- **Company**: Meta ([via careers page URL](https://www.metacareers.com/jobs/503684125178318/))
- **Role**: Software Engineer, iOS
- **XYZ Company Offering**: A dedicated software development engineer to Meta to help accelerate their hiring and development process.

### Output

```plaintext
Subject: Expert iOS Development Services for Your Mobile Teams

Dear Hiring Manager,

I came across your job posting for a Software Engineer, iOS, and I'm excited to introduce you to XYZ Company (meta 2), a leading AI & Software Consulting company that can help you build world-class iOS applications. With our expertise in mobile software development, we can support your mobile teams in creating elegant products that bring social experiences to hundreds of millions of people.

Our team of skilled iOS engineers has extensive experience in building complex applications targeting iOS in production using native languages and frameworks. We possess expertise in iOS SDK, user interfaces, infrastructure, tools supporting applications on the iPhone or iPad, multithreading programming, mobile memory management, and performance debugging and benchmarking.

At XYZ Company (meta 2), we have a proven track record of delivering high-quality mobile solutions that meet the needs of our clients. Our portfolio includes:

* https://henrywhite.dev (a personal website built using modern web technologies)
* https://charlielee.tech (a tech blog featuring articles on software development and technology trends)
* https://oliviacooper.dev (a personal website showcasing expertise in web development)

These projects demonstrate our capabilities in building scalable, efficient, and user-friendly applications. We can bring the same level of expertise to your iOS development projects.

By partnering with us, you can leverage our expertise to:

* Build high-performance iOS applications that meet your business needs
* Enhance your mobile teams' capabilities with our experienced engineers
* Reduce development time and costs with our efficient development processes

If you're looking for a reliable partner to help you build world-class iOS applications, I'd love to schedule a call to discuss how meta can support your mobile teams.

Please let me know if you're interested, and I'll be happy to set up a call at your convenience.

Best regards,  
Max  
Business Development Executive  
XYZ Company (meta 2)
