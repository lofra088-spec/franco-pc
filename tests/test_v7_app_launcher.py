from pathlib import Path

from franco.v7.app_launcher import WindowsAppLauncher


def test_start_menu_fuzzy_match_launches_best_shortcut(tmp_path: Path):
    root = tmp_path / "Programs"
    root.mkdir()
    obs = root / "OBS Studio.lnk"
    discord = root / "Discord.lnk"
    obs.write_bytes(b"shortcut")
    discord.write_bytes(b"shortcut")
    launched = []
    launcher = WindowsAppLauncher(roots=[root], startfile=launched.append,
                                  environ={}, popen=lambda *a, **k: None)

    label = launcher.launch("avvia obs studio".removeprefix("avvia "))

    assert label == "OBS Studio"
    assert launched == [str(obs.resolve())]


def test_unknown_application_is_reported_instead_of_claiming_success(tmp_path: Path):
    launcher = WindowsAppLauncher(roots=[tmp_path], startfile=lambda _p: None,
                                  environ={}, popen=lambda *a, **k: None)
    try:
        launcher.launch("app che non esiste")
    except LookupError as exc:
        assert "non trovata" in str(exc)
    else:
        raise AssertionError("unknown application was accepted")


def test_executable_is_started_from_its_own_directory(tmp_path: Path):
    exe = tmp_path / "bin" / "64bit" / "obs64.exe"
    exe.parent.mkdir(parents=True)
    exe.write_bytes(b"binary")
    calls = []
    launcher = WindowsAppLauncher(roots=[], environ={}, startfile=lambda _p: None,
                                  popen=lambda *args, **kwargs: calls.append((args, kwargs)))

    launcher.launch(str(exe))

    args, kwargs = calls[0]
    assert args == ([str(exe.resolve())],)
    assert kwargs["cwd"] == str(exe.parent.resolve())
    assert kwargs["shell"] is False
