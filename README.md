# **IBM Z DATATHON** 2025
# PROJECT NAME : SENTINEL-API

# Description of project:
Sentinel API is a security simulator that tests and verifies third-party APIs before deployment. It runs APIs in a controlled environment to detect bugs, vulnerabilities, and suspicious activities. By ensuring only secure APIs go live, Sentinel API reduces risks of data breaches, fraud, and unauthorised access — enabling faster, safer, and more reliable integrations.

# Problem Statement:
Industries such as finance, e-commerce, education, government, and healthcare now depend heavily on third-party APIs to deliver seamless services and encourage innovation. While APIs make it easier for organizations to collaborate and boost efficiency, they also introduce serious risks. If an API is compromised by malware, logic errors, or poor integration, it can lead to cyberattacks that impact both organizations and their users.

End-users, who have no thought about the security of APIs, are the ones who suffer the most. Just one weak API can set off a chain of events that lead to financial fraud, identity theft, privacy violations, and interruption of the basic services. A recent case serves as a good example of this danger: in September 2025, the fintech company Flexy Pay, located in Hyderabad, was hit by a fraud of ₹1.3 crore due to the misuse of Yes Bank's APIs, which allowed unauthorised transactions through suspicious requests from whitelisted IPs. This event is a perfect example of why we need to fix API security holes as soon as possible. While APIs have become the backbone of many organizational structures, the majority of these organizations do not have any proper testing and review systems in place for their APIs before actual implementation. 

Instead of focusing on the safety of their users, most teams concentrate on fast launches. A smart way to win and retain user trust is for companies to deploy reliable security solutions that guarantee the security and stability of their APIs, regardless of which sector they belong to.


# Data set:
Since no public dataset exists for malicious API URLs, we enhanced existing malicious URL datasets by transforming them into API-like patterns to simulate realistic API traffic. This allows our model — API Sentinel — to accurately detect malicious API endpoints based on learned domain and path features.
 
## Solution:
We have come up with a model of a simulator that serves as a point of verification for APIs before they are implemented in the market. The process will be that APIs are not directly integrated but first, they are introduced in a controlled environment in which their behavior, requests, and responses are monitored. The simulator looks for bugs, unusual activities, and security vulnerabilities, among other things, and therefore, only safe APIs pass the checkpoint.

Such a methodology lowers the chances of fraud, leakage of data, and unauthorized access of which trust among users is the positive outcome. Organizations can make the deployments quicker and safer, while the users are protected from the latent threats. Our solution, by early API verification, establishes a harmony between technology and safety all over the globe.


# Mind Map:

![WhatsApp Image 2025-09-27 at 09 57 30_26e53010](https://github.com/user-attachments/assets/eaab8efc-55da-4013-a7b0-56ea3b988461)

# Leveraging the IBM-Z technology for the solution:

IBM-Z provided a powerful and secure environment for developing and testing the Sentinel API simulator. Its advanced computing capabilities and integrated resource packages allowed us to handle large-scale API data efficiently while performing accelerated vulnerability analysis. Using IBM-Z, we simulated multiple API requests and monitored their behavior in real time, enabling faster detection of anomalies and security flaws. The platform’s high reliability and performance ensured accurate testing results, helping us build a robust system that validates APIs with speed, precision, and scalability.




# This repository contains the source code of the project work from the past 24 hours.

## Data Preprocessing & Feature Extraction:

1. API URLs are decomposed into subdomain, domain, and path components for granular analysis.

2. Normalisation and tokenization are applied to extract meaningful patterns.

## Descriptive & Exploratory Analysis:

1. Statistical and behavioural summaries of benign vs. malicious APIs.

2. Visualisation of API patterns and distribution across threat levels.

## Model Training & Evaluation:

1. Multiple classification algorithms are trained to detect malicious APIs.

2. Model performance is evaluated using accuracy, precision, recall, and F1-score.

## Frontend Integration:

1. The trained model is connected to a frontend interface where users can paste an API URL.

2. The system instantly predicts whether the API is safe or malicious, providing a real-time security check.



# Some Insights from the Jupyter Notebook that we found useful!
![WhatsApp Image 2025-10-11 at 23 19 22_bbc88f2f](https://github.com/user-attachments/assets/24e4c784-837c-47c5-a2f3-0fea1ce85c52)

![WhatsApp Image 2025-10-11 at 23 19 22_9fa789ef](https://github.com/user-attachments/assets/4f4d0405-634e-46c7-a6ac-cfbac0584aa2)


![WhatsApp Image 2025-10-11 at 23 19 21_f3f25677](https://github.com/user-attachments/assets/21dad905-0998-4226-af6f-df6d89591973)

<img width="1919" height="969" alt="Screenshot 2025-10-11 230355 1" src="https://github.com/user-attachments/assets/d8cf949c-6cef-4910-9812-506f6e3e5708" />

![WhatsApp Image 2025-10-11 at 23 17 16_f5128531](https://github.com/user-attachments/assets/e1f2d1d3-0015-472e-a4b5-c230993b0077)
![WhatsApp Image 2025-10-11 at 23 17 44_401ca9f7](https://github.com/user-attachments/assets/6d30ea5d-08ab-4561-b052-5517a45f767b)

![WhatsApp Image 2025-10-11 at 23 16 26_1969561d](https://github.com/user-attachments/assets/c38a8aa3-00f2-46db-846e-ed4d440e9884)

# Video Explanation for the project:

https://user-images.githubusercontent.com/64836894/134806280-9133cd2c-5aee-4b22-b59e-2182dfc2479d.mp4

# Conclusion :
The Sentinel API guarantees the secure deployment of third-party APIs by detecting vulnerabilities through advanced simulations and machine learning techniques.Leveraging the power of IBM-Z, it provides rapid, scalable, and dependable security validation.This strengthens user trust and protects organizations from API-related threats effectively.
