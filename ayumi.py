import win32com.client
sapi = win32com.client.Dispatch("SAPI.SpVoice")
cat  = win32com.client.Dispatch("SAPI.SpObjectTokenCategory")
cat.SetID(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", False)
v = [t for t in cat.EnumerateTokens() if t.GetAttribute("Name") == "Microsoft Ayumi"]
if v:
    oldv = sapi.Voice
    sapi.Voice = v[0]
    sapi.Speak("高校生のTiktokと同じやつつかってくにさんも出してた")
    sapi.Voice = oldv