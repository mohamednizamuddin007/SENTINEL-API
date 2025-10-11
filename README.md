# **IBM z DATATHON**
# SENTINAL-API

## Description of project:
Sentinel API is a security simulator that tests and verifies third-party APIs before deployment. It runs APIs in a controlled environment to detect bugs, vulnerabilities, and suspicious activities. By ensuring only secure APIs go live, Sentinel API reduces risks of data breaches, fraud, and unauthorized access — enabling faster, safer, and more reliable integrations.


## Mind Map:

![WhatsApp Image 2025-09-27 at 09 57 30_26e53010](https://github.com/user-attachments/assets/eaab8efc-55da-4013-a7b0-56ea3b988461)


## Problem Statement:
Industries such as finance, e-commerce, education, government, and healthcare now depend heavily on third-party APIs to deliver seamless services and encourage innovation. While APIs make it easier for organizations to collaborate and boost efficiency, they also introduce serious risks. If an API is compromised by malware, logic errors, or poor integration, it can lead to cyberattacks that impact both organizations and their users.

End-users, who have no thought about the security of APIs, are the ones who suffer the most. Just one weak API can set off a chain of events that lead to financial fraud, identity theft, privacy violations, and interruption of the basic services. A recent case is a good example to show this danger: in September 2025, a fintech company Flexy pay located in Hyderabad was hit by a fraud of ₹1.3 crore due to the misuse of Yes Bank's APIs, where unauthorized transactions were allowed by suspicious requests from the whitelisted IPs. This event is a perfect example that we need to fix API security holes as soon as possible. While APIs have become the backbone of many organizational structures, the majority of these organizations do not have any proper testing and review systems in place for their APIs before actual implementation. 

Instead of focusing on the safety of their users, most teams concentrate on fast launches. A smart way to win and retain user trust is for companies to deploy reliable security solutions that guarantee the security and stability of their APIs regardless of which sector they belong to.


## Data set:
We have gathered a dataset built by augmenting datasets of rainfall, climate and fertilizer data available from github. we hope this gives us a better idea of the trends of crops considering different environmental and geographical factors.

 
## Solution:
We have come up with a model of a simulator that serves as a point of verification for APIs before they are implemented in the market. The process will be that APIs are not directly integrated but first, they are introduced in a controlled environment in which their behavior, requests, and responses are monitored. The simulator looks for bugs, unusual activities, and security vulnerabilities among other things, and therefore, only safe APIs pass the checkpoint.

Such a methodology lowers the chances of fraud, leakage of data, and unauthorized access of which trust among users is the positive outcome. Organizations can make the deployments quicker and safer, while the users are protected from the latent threats. Our solution, by early API verification, establishes a harmony between technology and safety all over the globe.


## Leveraging the IBM-Z technology to the solution:

IBM-Z provided a powerful and secure environment for developing and testing the Sentinel API simulator. Its advanced computing capabilities and integrated resource packages allowed us to handle large-scale API data efficiently while performing accelerated vulnerability analysis. Using IBM-Z, we simulated multiple API requests and monitored their behavior in real time, enabling faster detection of anomalies and security flaws. The platform’s high reliability and performance ensured accurate testing results, helping us build a robust system that validates APIs with speed, precision, and scalability.




### This repository contains the source code of the project work from past 24 hours.
The Jupyter Notebook contains:

1. Descriptive Analysis of the Agriculture Data.
    i)checking summary of crops such as average of various parameters.
    ii)summary statistics of indivisual crop. using Interactive function to choose.
    iii)Average requirnment for each crop with given conditions.

2. Analysis of different agcriculture
    i)conditions using disc plot

3. categories the crop based on season clustering similar kind of crops
    using hard and soft clustering techniques.

4. Finding out any hiding Patterns in the Dataset.

5. Predictive Modeling.




## Some Insights from the Jupyter Notebook that we found useful!
![WhatsApp Image 2025-10-10 at 23 15 20_f0cd609f](https://github.com/user-attachments/assets/d85dc0da-5b77-432d-a2ce-4fd1392857bf)

![WhatsApp Image 2025-10-10 at 22 59 16_3afc26f5](https://github.com/user-attachments/assets/1a023e56-235a-44fa-af9d-a0f7ff228f33)



![Screenshot (34)](https://user-images.githubusercontent.com/64836894/134804195-0d430414-deb9-44c3-abe0-541ec1c15a52.png)
![Screenshot (33)](https://user-images.githubusercontent.com/64836894/134804196-caede5cf-f883-40b9-ae55-6c4abe4ed3a2.png)
![Screenshot (32)](https://user-images.githubusercontent.com/64836894/134804198-59f9bcf0-125c-4716-b139-ce3ad836502a.png)
![prediction ](https://user-images.githubusercontent.com/69135317/134804507-2e1637ea-d007-4fc2-836e-3ec0a6635126.png)

## Video Explation for the project:

https://user-images.githubusercontent.com/64836894/134806280-9133cd2c-5aee-4b22-b59e-2182dfc2479d.mp4

