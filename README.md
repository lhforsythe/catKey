# catKey

![catKey](https://github.com/lhforsythe/catKey/blob/main/icon-white.png?raw=true)

A keyboard input toggle for when your cat decides its nap time. **Only works on Hyprland

## About
My cat wanted to sleep on my keyboard, and I needed a quick way of toggling it off without resorting to ripping out the USB cable before my work was consumed by cat-gibberish. Thus, I created a simple python script that interfaces with `hyprctl`' to block and unblock input from a specified keyboard. It uses QT to create a system tray icon, which should be visible from any system tray. Note that, by default, it blocks the first keyboard that shows up when `hyprctl devices` is run. If you want a different device, at least for now, just change the index from 0 to a different number corresponding to the correct keyboard, where 0 means the first keyboard that shows up.
## Usage
1) Clone the repository
2) CD to the downloaded folder
3) Run the script (make sure you are in the same folder as the repository, else it will fail to find the icons)
4) Click the little cat in the system tray to toggle the keyboard input. Black cat means keyboard is blocked, white cat means keyboard is active.
