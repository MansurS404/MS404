# RECODE = MUHAMMAD RIZKY
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
