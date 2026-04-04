# Reddit Terminal Media Uploader

A CLI tool designed for power users and content creators to upload high-quality photos and videos to Reddit directly from the terminal. 

## Why this isn't on Devvit
This tool requires access to the **local file system** to read media buffers and a **Command Line Interface (CLI)** for workflow integration, both of which are currently unsupported by the Reddit Devvit sandboxed environment.

## Features
- CLI-based authentication via OAuth2.
- Support for image and video uploads.
- Automatic subreddit-specific flair handling.
- Bypasses web-based GUI for faster creator workflows.

## Tech Stack
- **Language:** Python 3.10+
- **Library:** PRAW (Python Reddit API Wrapper)
- **API Endpoints:** `/api/upload_media`, `/api/submit`