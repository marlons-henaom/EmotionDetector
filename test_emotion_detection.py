from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_emotion_detection(unittest.TestCase):
    def test_emotion_detection(self):

        # Test 1
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result["dominant_emotion"], "joy")

        # Test 2
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result["dominant_emotion"], "anger")

        # Test 3
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result["dominant_emotion"], "disgust")

        # Test 4
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result["dominant_emotion"], "sadness")

        # Test 5
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result["dominant_emotion"], "fear")

unittest.main()