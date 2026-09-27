import unittest
from genpark_voice_vad import VoiceTurnTakingEndpointDetector as Client

class CoreTests(unittest.TestCase):

    def test_active_and_endpoint(self):
        c = Client()
        self.assertEqual(c.analyze_turn_status([-20], "Hello.", 800)["decision"], "CONTINUE_LISTENING")
        self.assertEqual(c.analyze_turn_status([-55], "Hello.", 800)["decision"], "ENDPOINT_DETECTED")
    def test_multiword_hesitation(self):
        self.assertTrue(Client().predict_semantic_closure("I was thinking you know")["is_trailing_hesitation"])
    def test_empty_and_calibration(self):
        c = Client()
        self.assertEqual(c.predict_semantic_closure("")["semantic_completion_score"], 0)
        self.assertEqual(c.calibrate_acoustic_thresholds([-50, -52])["calibrated_speech_threshold_db"], -37)

if __name__ == "__main__": unittest.main()
