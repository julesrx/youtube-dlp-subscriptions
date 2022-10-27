# youtube-dlp-subscriptions

Downloads new videos from your YouTube subscription feeds since the last run.

## Requirements

This script requires either docker and docker compose or python3.

## Usage

First off, clone the repository and cd into it:

```console
git clone https://github.com/julesrx/youtube-dlp-subscriptions
cd youtube-dlp-subscriptions
```

Create a `channels.txt` file inside `downloads/` and populate it with your channels to download from. See `channels.txt` for an example.  
The only factor that you must change is the CHANNEL_ID. The text before is only for self-comments (and is useful for maintaining a long list).

### Docker-Compose

If you are familiar with what docker is, and what docker-compose is to docker, this is the recommended method to use.  
Start the process: `docker-compose up`

### Manual

This method requires python3.  
Run the bash script: `./run.sh`

## SyncThing

Syncthing can be set up to sync from the downloads folder onto any other device (such as an android). Quite useful for long trips without cellular internet (or a data plan).

## Automation

A cron job can be set up to run the process at specified intervals. Be sure to cd into the directory first before running docker run from cron.

i.e: every day at 2AM, log stdout/stderr to log as well

```cron
0 2 * * * cd <path-to-script>/ && docker-compose up 2>&1 | tee log.txt
```

## Thanks

A thanks to [@mewfree](https://github.com/mewfree) for the [original script](https://github.com/mewfree/youtube-dl-subscriptions) and [@pukkandan](https://github.com/pukkandan) for [dlp](https://github.com/yt-dlp/yt-dlp).
