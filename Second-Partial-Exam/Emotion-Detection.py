import re
import numpy as np
from collections import defaultdict


class EmotionDetector:
    def __init__(self):
        # Prior probabilities P(E)
        self.prior_probabilities = {
            'happy': 0.4,
            'sad': 0.3,
            'angry': 0.3
        }

        # Conditional probabilities P(W|E)
        self.conditional_probabilities = {
            'happy': {
                'happy': 0.25,
                'joyful': 0.125,
                'great': 0.125,
                'sad': 0.05,
                'down': 0.03,
                'angry': 0.02,
                'mad': 0.01,
                'frustrated': 0.005
            },
            'sad': {
                'happy': 0.05,
                'joyful': 0.02,
                'great': 0.03,
                'sad': 0.20,
                'down': 0.125,
                'angry': 0.03,
                'mad': 0.02,
                'frustrated': 0.01
            },
            'angry': {
                'happy': 0.10,
                'joyful': 0.03,
                'great': 0.02,
                'sad': 0.05,
                'down': 0.02,
                'angry': 0.15,
                'mad': 0.125,
                'frustrated': 0.10
            }
        }

        # Small value for smoothing (handle words not in vocabulary)
        self.smoothing_value = 0.001

    def preprocess_text(self, text):
        """Clean and preprocess the text"""
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation and split into words
        words = re.findall(r'\b\w+\b', text)
        return words

    def calculate_probability(self, message):
        """Calculate P(E|W) for each emotion given the message"""
        words = self.preprocess_text(message)

        # Store posterior probabilities for each emotion
        posterior_probabilities = {}

        # Calculate P(W) - probability of the message
        p_message = 0
        for emotion in self.prior_probabilities:
            p_emotion = self.prior_probabilities[emotion]

            # Calculate P(W|E) - probability of words given emotion
            p_words_given_emotion = 1.0
            for word in words:
                if word in self.conditional_probabilities[emotion]:
                    p_words_given_emotion *= self.conditional_probabilities[emotion][word]
                else:
                    # Apply smoothing for unknown words
                    p_words_given_emotion *= self.smoothing_value

            # P(W) += P(W|E) * P(E)
            p_message += p_words_given_emotion * p_emotion

            # Store P(W|E) * P(E) for later use
            posterior_probabilities[emotion] = p_words_given_emotion * p_emotion

        # If p_message is 0, all words were unknown
        if p_message == 0:
            return {emotion: self.prior_probabilities[emotion] for emotion in self.prior_probabilities}

        # Calculate P(E|W) = P(W|E) * P(E) / P(W)
        for emotion in posterior_probabilities:
            posterior_probabilities[emotion] /= p_message

        return posterior_probabilities

    def detect_emotion(self, message):
        """Detect the most probable emotion for a given message"""
        probabilities = self.calculate_probability(message)

        # Find emotion with highest probability
        most_probable_emotion = max(probabilities, key=probabilities.get)

        return most_probable_emotion, probabilities


# Test the emotion detector
def main():
    detector = EmotionDetector()

    while True:
        message = input("\nEnter a message (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break

        emotion, probabilities = detector.detect_emotion(message)

        print(f"\nDetected emotion: {emotion.upper()}")
        print("\nProbabilities:")
        for e, p in probabilities.items():
            print(f"  {e}: {p:.4f} ({p * 100:.2f}%)")


if __name__ == "__main__":
    main()