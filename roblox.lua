local PORT = 6969
local SystemLibrary = {}

local ws = WebSocket.connect("ws://localhost:"..PORT)

if ws then
    print("[DEBUG]: Connected Successfully!")
else
    print("[DEBUG]: Couldn't Connect, are you sure you have the server hosted?")
    return
end

function SystemLibrary:Shutdown()
    ws:Send("shutdown")
end

function SystemLibrary:Sleep()
    ws:Send("Sleep")
end

function SystemLibrary:KillRoblox()
    ws:Send("kill_roblox")
end

function SystemLibrary:Disconnect()
    ws:Close()
end

return SystemLibrary