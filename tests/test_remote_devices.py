import ast
import json
from pathlib import Path
import re
import typing
import unittest
from unittest.mock import Mock

SOURCE = Path(__file__).resolve().parents[1] / "src/franco/_monolith.py"

class RemoteTests(unittest.TestCase):
    def setUp(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "RemoteDeviceController")
        self.http = Mock()
        ns = dict(vars(typing), re=re, json=json, requests=self.http)
        exec(compile(ast.Module(body=[cls], type_ignores=[]), str(SOURCE), "exec"), ns)
        self.db = Mock()
        self.db.get_all_devices.return_value = []
        self.db.add_device.return_value = 1
        self.ctrl = ns["RemoteDeviceController"](Mock(), self.db, Mock())

    def test_ipad_registration_and_private_random_topic(self):
        self.ctrl.handle("aggiungi dispositivo Tablet salotto ipad")
        args = self.db.add_device.call_args.args
        self.assertEqual(args[0], "Tablet salotto")
        self.assertEqual(args[2], "ios")
        self.assertRegex(args[3], r"^franco_[a-f0-9]{32}$")

    def test_invalid_android_address(self):
        self.ctrl.handle("aggiungi dispositivo Samsung android")
        self.db.add_device.assert_not_called()

    def test_notification_is_not_execution(self):
        self.db.get_all_devices.return_value = [dict(device_name="personale", platform="ios", address="topic_test", authorized=True)]
        result = self.ctrl.handle("blocca personale")
        self.assertIn("esecuzione non confermata", result)
        self.http.post.return_value.raise_for_status.assert_called_once()
        self.db.touch_device_seen.assert_not_called()
        payload = self.http.post.call_args.kwargs["json"]
        self.assertEqual(payload["actions"][0]["url"], "shortcuts://run-shortcut?name=Blocca")

    def test_http_failure(self):
        self.http.post.return_value.raise_for_status.side_effect = RuntimeError("503")
        ok, info = self.ctrl._ios_action(dict(address="topic_test"), "lock", "blocca")
        self.assertFalse(ok)
        self.assertIn("fallito", info)

    def test_revoked_device_not_contacted(self):
        self.db.get_all_devices.return_value = [dict(device_name="personale", platform="ios", authorized=False)]
        self.ctrl.handle("blocca personale")
        self.http.post.assert_not_called()
        self.ctrl.handle("revoca dispositivo personale")
        self.db.set_device_authorized.assert_called_once_with("personale", False)

    def test_multiple_iphones_require_name(self):
        self.db.get_all_devices.return_value = [dict(device_name=n, platform="ios") for n in ("uno", "due")]
        self.assertEqual(self.ctrl._match_devices("blocca iphone"), [])

    def test_custom_shortcut(self):
        self.ctrl._ios_action(dict(address="topic_test"), "shortcut", "esegui scorciatoia Modalita Lettura su personale")
        url = self.http.post.call_args.kwargs["json"]["actions"][0]["url"]
        self.assertIn("modalita+lettura", url)

if __name__ == "__main__":
    unittest.main()
