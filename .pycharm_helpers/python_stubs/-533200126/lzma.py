# encoding: utf-8
# module lzma
# from /usr/lib64/python2.7/site-packages/lzma.so
# by generator 1.145
"""
The python lzma module provides a comprehensive interface for
the lzma compression library. It implements one shot (de)compression
functions, CRC-32 & CRC-64 checksum computations, types for sequential
(de)compression, and advanced options for lzma compression.
"""
# no imports

# Variables with simple values

LZMA_FINISH = 3

LZMA_FULL_FLUSH = 2

LZMA_RUN = 0

LZMA_SYNC_FLUSH = 1

LZMA_VERSION = '5.1.2alpha'

__author__ = 'The lzma python module was written by:\n\n    Per \xc3\x98yvind Karlsen <peroyvind@mandriva.org>\n'

__version__ = '0.5.3'

# functions

def compress(string, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    compress(string [, options={'format':'xz', 'check':'crc32', 'level':6, 'extreme':False,
    'dict_size':23, 'lc':3 'lp':0, 'pb':2, 'mode':2,
    'nice_len':128, 'mf':'bt4', 'depth':0]) -> string
    
    Compress data using the given parameters, returning a string
    containing the compressed data.
    """
    pass

def crc32(string, start=None): # real signature unknown; restored from __doc__
    """
    crc32(string[, start]) -> int
    
    Compute a CRC-32 checksum of string.
    
    An optional starting value 'start' can be specified.
    """
    return 0

def crc64(string, start=None): # real signature unknown; restored from __doc__
    """
    crc64(string[, start]) -> int
    
    Compute a CRC-64 checksum of string.
    
    An optional starting value 'start' can be specified.
    """
    return 0

def decompress(string, bufsize=8192, memlimit=-1): # real signature unknown; restored from __doc__
    """
    decompress(string[, bufsize=8192, memlimit=-1]) -> string
    
    Decompress data in one shot. If you want to decompress data sequentially,
    use an instance of LZMADecompressor instead.
    
    Optional arg 'bufsize' is the initial output buffer size.
    Optional arg 'memlimit' is the maximum amount of memory the decoder may use,
    -1 means no limit.
    """
    return ""

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class LZMACompressor(object):
    """
    LZMACompressor([options={'format':'xz', 'check':'crc32', 'level':6, 'extreme':False,
    'dict_size':23, 'lc':3 'lp':0, 'pb':2, 'mode':2,
    'nice_len':128, 'mf':'bt4', 'depth':0]) -> compressor object
    Create a new compressor object. This object may be used to compress
    data sequentially. If you want to compress data in one shot, use the
    compress() function instead.
    """
    def compress(self, data): # real signature unknown; restored from __doc__
        """
        compress(data) -> string
        
        Feed the compressor object with data to compress sequently.
        This function will return the header for the compressed string for the first
        input provided, this header will be needed to concatenate with the rest of
        the stream when flushing to have a proper stream able to be decompressed
        again.
        """
        return ""

    def flush(self, mode=None): # real signature unknown; restored from __doc__
        """
        flush( [mode] ) -> string
        
        Returns a string containing any remaining compressed data.
        
        'mode' can be one of the constants LZMA_SYNC_FLUSH, LZMA_FULL_FLUSH, LZMA_FINISH; the
        default value used when mode is not specified is LZMA_FINISH.
        If mode == LZMA_FINISH, the compressor object can no longer be used after
        calling the flush() method.  Otherwise, more data can still be compressed.
        """
        return ""

    def reset(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        reset([options={'format':'xz', 'check':'crc32', 'level':6, 'extreme':False,
        'dict_size':23, 'lc':3 'lp':0, 'pb':2, 'mode':2,
        'nice_len':128, 'mf':'bt4', 'depth':0]) -> None
        
        Resets the compression object keeping the compression settings.
        These existing settings can be overriden by providing
        keyword settings.
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    lzma_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary containing the lzma encoder options."""



class LZMADecompressor(object):
    """
    LZMADecompressor([max_length=0, memlimit=-1]) -> decompressor object
    
    Create a new decompressor object. This object may be used to decompress
    data sequentially. If you want to decompress data in one shot, use the
    decompress() function instead.
    """
    def decompress(self, data, max_length=0): # real signature unknown; restored from __doc__
        """
        decompress(data[, max_length=0]) -> string
        
        Return a string containing the decompressed version of the data.
        
        After calling this function, some of the input data may still be stored in
        internal buffers for later processing.
        Call the flush() method to clear these buffers.
        If the max_length parameter is specified then the return value will be
        no longer than max_length. Unconsumed input data will be stored in
        the unconsumed_tail data descriptor.
        """
        return ""

    def flush(self, flushmode=None, bufsize=None): # real signature unknown; restored from __doc__
        """
        flush( [flushmode=LZMA_FINISH, bufsize] ) -> string
        
        Return a string containing any remaining decompressed data.
        'bufsize', if given, is the initial size of the output buffer.
        
        The decompressor object can only be used again after this call
        if reset() is called afterwards.
        """
        return ""

    def reset(self, maxlength=0, memlimit=-1): # real signature unknown; restored from __doc__
        """
        reset([maxlength=0, memlimit=-1]) -> None
        
        Resets the decompression object.
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, max_length=0, memlimit=-1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    unconsumed_tail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unused_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LZMAFile(object):
    """
    LZMAFile(name [, mode='r', buffering=0, memlimit=-1,
    options={'format':'xz', 'check':'crc32', 'level':6, 'extreme':False,
    'dict_size':23, 'lc':3 'lp':0, 'pb':2, 'mode':2,
    'nice_len':128, 'mf':'bt4', 'depth':0]) -> file object
    
    Open a lzma file. The mode can be 'r' or 'w', for reading (default) or
    writing. When opened for writing, the file will be created if it doesn't
    exist, and truncated otherwise. If the buffering argument is given, 0 means
    unbuffered, and larger numbers specify the buffer size.
    
    Add a 'U' to mode to open the file for input with universal newline
    support. Any line ending in the input file will be seen as a '\n' in
    Python. Also, a file so opened gains the attribute 'newlines'; the value
    for this attribute is one of None (no newline read yet), '\r', '\n',
    '\r\n' or a tuple containing all the newline types seen. Universal
    newlines are available only when reading.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None or (perhaps) an integer
        
        Close the file. Sets data attribute .closed to true. A closed file
        cannot be used for further I/O operations. close() may be called more
        than once without error.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read(self, size=None): # real signature unknown; restored from __doc__
        """
        read([size]) -> string
        
        Read at most size uncompressed bytes, returned as a string. If the size
        argument is negative or omitted, read until EOF is reached.
        """
        return ""

    def readline(self, size=None): # real signature unknown; restored from __doc__
        """
        readline([size]) -> string
        
        Return the next line from the file, as a string, retaining newline.
        A non-negative size argument will limit the maximum number of bytes to
        return (an incomplete line may be returned then). Return an empty
        string at EOF.
        """
        return ""

    def readlines(self, size=None): # real signature unknown; restored from __doc__
        """
        readlines([size]) -> list
        
        Call readline() repeatedly and return a list of lines read.
        The optional size argument, if given, is an approximate bound on the
        total number of bytes in the lines returned.
        """
        return []

    def seek(self, offset, whence=None): # real signature unknown; restored from __doc__
        """
        seek(offset [, whence]) -> None
        
        Move to new file position. Argument offset is a byte count. Optional
        argument whence defaults to 0 (offset from start of file, offset
        should be >= 0); other values are 1 (move relative to current position,
        positive or negative), and 2 (move relative to end of file, usually
        negative, although many platforms allow seeking beyond the end of a file).
        
        Note that seeking of lzma files is emulated, and depending on the parameters
        the operation may be extremely slow.
        """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """
        tell() -> int
        
        Return the current file position, an integer (may be a long integer).
        """
        return 0

    def write(self, data): # real signature unknown; restored from __doc__
        """
        write(data) -> None
        
        Write the 'data' string to file. Note that due to buffering, close() may
        be needed before the file on disk reflects the data written.
        """
        pass

    def writelines(self, sequence_of_strings): # real signature unknown; restored from __doc__
        """
        writelines(sequence_of_strings) -> None
        
        Write the sequence of strings to the file. Note that newlines are not
        added. The sequence can be any iterable object producing strings. This is
        equivalent to calling write() for each string.
        """
        pass

    def xreadlines(self): # real signature unknown; restored from __doc__
        """
        xreadlines() -> self
        
        For backward compatibility. LZMAFile objects now include the performance
        optimizations previously implemented in the xreadlines module.
        """
        return self

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ __enter__() -> self. """
        return self

    def __exit__(self, *excinfo): # real signature unknown; restored from __doc__
        """ __exit__(*excinfo) -> None.  Closes the file. """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, name, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed"""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """file mode ('r', 'w', or 'U')"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """file name"""

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """end-of-line convention used in this file"""

    softspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """flag indicating that a space needs to be printed; used by print"""



class LZMAOptions(object):
    """
    This class describes the different LZMA compression options and holds the
    different min and max value constants for these in the variables.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of integrity check to use (XZ format only):
'crc32': CRC32 using the polynomial from the IEEE 802.3 standard. (default)
'crc64': CRC64 using the polynomial from the ECMA-182 standard.
'sha256': SHA-256.
"""

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Depth (also known as match finder cycles)
Higher values give slightly better compression ratio but
decrease speed. Use special value 0 to let liblzma use
match-finder-dependent default value.
"""

    dict_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary size in bytes (4096 - 1610612736)
Dictionary size indicates how many bytes of the recently processed
uncompressed data is kept in memory. One method to reduce size of
the uncompressed data is to store distance-length pairs, which
indicate what data to repeat from the dictionary buffer. Thus,
the bigger the dictionary, the better compression ratio usually is.
"""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File format to use for compression:
'xz': XZ format used by new xz tool. (default)
'alone': LZMA_Alone format used by older lzma utils.
"""

    lc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of literal context bits (0 - 4)
How many of the highest bits of the previous uncompressed
eight-bit byte (also known as `literal') are taken into
account when predicting the bits of the next literal.

There is a limit that applies to literal context bits and literal
position bits together: lc + lp <= 4. Without this limit the
decoding could become very slow, which could have security related
results in some cases like email servers doing virus scanning."""

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Compression preset level (0 - 9)
This will automatically set the values for the various compression options.
Setting any of the other compression options at the same time as well will
override the specific value set by this preset level.

Preset level settings:
level	 lc	 lp	 pb	 mode	 mf	 nice_len	 depth	 dict_size
9	 3	 0	 2	 normal	 bt4	 64		 0	 67108864
8	 3	 0	 2	 normal	 bt4	 64		 0	 33554432
7	 3	 0	 2	 normal	 bt4	 64		 0	 16777216
6	 3	 0	 2	 normal	 bt4	 64		 0	 8388608
5	 3	 0	 2	 normal	 bt4	 32		 0	 8388608
4	 3	 0	 2	 normal	 bt4	 16		 0	 4194304
3	 3	 0	 2	 fast	 hc4	 273		 48	 4194304
2	 3	 0	 2	 fast	 hc4	 273		 24	 2097152
1	 3	 0	 2	 fast	 hc4	 128		 8	 1048576
0	 3	 0	 2	 fast	 hc3	 128		 4	 262144
"""

    lp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of literal position bits (0 - 4)
How many of the lowest bits of the current position (number
of bytes from the beginning of the uncompressed data) in the
uncompressed data is taken into account when predicting the
bits of the next literal (a single eight-bit byte).
"""

    mf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Match finder has major effect on both speed and compression ratio.
Usually hash chains are faster than binary trees.
Available match finders:
'bt2': Binary Tree with 2 bytes hashing
       Memory requirements: 9.5 * dict_size + 4 MiB
'bt3': Binary Tree with 3 bytes hashing
       Memory requirements: 11.5 * dict_size + 4 MiB
'bt4': Binary Tree with 4 bytes hashing
       Memory requirements: 11.5 * dict_size + 4 MiB
'hc3': Hash Chain with 3 bytes hashing
'hc4': Hash Chain with 4 bytes hashing
       Memory requirements: 7.5 * dict_size + 4 MiB
"""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Available modes: 'fast' or 'normal'.
Fast mode is usually at its best when combined with a hash chain match finder.
Best is usually notably slower than fast mode. Use this together with binary
tree match finders to expose the full potential of the LZMA encoder."""

    nice_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nice lengt of a match (also known as number of fast bytes) (5 - 273)
Nice length of match determines how many bytes the encoder
compares from the match candidates when looking for the best
match. Bigger fast bytes value usually increase both compression
ratio and time.
"""

    pb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of position bits Position bits (0 - 4)
How many of the lowest bits of the current position in the
uncompressed data is taken into account when estimating
probabilities of matches. A match is a sequence of bytes for
which a matching sequence is found from the dictionary and
thus can be stored as distance-length pair.

Example: If most of the matches occur at byte positions
of 8 * n + 3, that is, 3, 11, 19, ... set pos_bits to 3,
because 2**3 == 8.
"""



# variables with complex values

options = None # (!) real value is ''

