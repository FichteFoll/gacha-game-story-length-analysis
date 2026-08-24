# Cookie flags for yt-dlp, opted into through the environment.
#
# YouTube starts answering "Sign in to confirm you're not a bot" after a few
# hundred full extractions, and the block is on the client rather than on the
# video: a request carrying a signed-in session is what gets through it. Solving
# the captcha in a browser lifts it for a while, but only the browser's cookies
# carry the result to yt-dlp.
#
#   YTDLP_COOKIES=<file>               a cookies.txt exported once, or
#   YTDLP_COOKIES_FROM_BROWSER=<name>  yt-dlp reads the browser's own store
#                                      (firefox, chrome, chromium, brave, ...)
#
# Neither is set by default, so the pipeline stays anonymous unless someone opts
# in. Use a throwaway account: this is automated extraction at a few hundred
# requests a run, and it is the session that wears the consequences.
#
# Sets the array YT_AUTH rather than wrapping yt-dlp, because every call site
# runs it under `timeout`, which executes a program and cannot be pointed at a
# shell function.
#
# The cookie file is copied per call, into the scratch path the caller passes.
# yt-dlp writes the jar back when it is done, and several jobs writing one file
# corrupts it; the copy also keeps the caller's own cookies.txt untouched.
yt_auth() {
  local scratch="${1:?yt_auth needs a scratch path for the cookie copy}"
  YT_AUTH=()
  if [[ -n "${YTDLP_COOKIES:-}" ]]; then
    cp -- "$YTDLP_COOKIES" "$scratch" && YT_AUTH+=(--cookies "$scratch")
  fi
  if [[ -n "${YTDLP_COOKIES_FROM_BROWSER:-}" ]]; then
    YT_AUTH+=(--cookies-from-browser "$YTDLP_COOKIES_FROM_BROWSER")
  fi
  return 0
}
export -f yt_auth
