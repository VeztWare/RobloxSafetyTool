# RobloxSafetyTool
A tool for staying AFK overnight in Roblox without having to worry about your house burning down or your components getting damaged. made by VeztWare

# Needs:
- WebSockets (executor)
- Windows OS
- WebSockets Package (pip install websockets)
- Hibernation Disabled (for sleeping)

# Usage:
- Run the "server.py" first and then loadstring the "roblox.lua" library in your executor (in-game)
- commands: "sleep", "shutdown", "kill_roblox"

# Documentary:
```
local system = loadstring(readfile("roblox.lua"))()

system:Shutdown() -- shutdown pc
system:Sleep() -- sleep pc
system:KillRoblox() -- kill roblox
```
