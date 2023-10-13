Misc resources for downloading 7p syzygy tablebases
when disk space is a limitation.

Syzygy 7-piece tablebases are freely available for download here:
https://tablebase.lichess.ovh/tables/standard/7/

Practical 7-piece tablebases in < 200 GB
https://groups.google.com/g/fishcooking/c/chP0S4jXTxU

5v2 with material difference <= 1

KBBPPvKQ
KBNPPvKQ
KNNPPvKQ
KRPPPvKQ

If you want to download all ~17 TB worth of data:

```sh
wget --mirror --no-parent --no-directories -e robots=off \
  https://tablebase.lichess.ovh/tables/standard/7/
```
