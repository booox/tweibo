#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Article:
  """
  Attributes:
   - title
   - description
   - imageurl
   - url
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'title', None, None, ), # 1
    (2, TType.STRING, 'description', None, None, ), # 2
    (3, TType.STRING, 'imageurl', None, None, ), # 3
    (4, TType.STRING, 'url', None, None, ), # 4
  )

  def __init__(self, title=None, description=None, imageurl=None, url=None,):
    self.title = title
    self.description = description
    self.imageurl = imageurl
    self.url = url

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.title = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.description = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.imageurl = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.url = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Article')
    if self.title is not None:
      oprot.writeFieldBegin('title', TType.STRING, 1)
      oprot.writeString(self.title)
      oprot.writeFieldEnd()
    if self.description is not None:
      oprot.writeFieldBegin('description', TType.STRING, 2)
      oprot.writeString(self.description)
      oprot.writeFieldEnd()
    if self.imageurl is not None:
      oprot.writeFieldBegin('imageurl', TType.STRING, 3)
      oprot.writeString(self.imageurl)
      oprot.writeFieldEnd()
    if self.url is not None:
      oprot.writeFieldBegin('url', TType.STRING, 4)
      oprot.writeString(self.url)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class News:
  """
  Attributes:
   - title
   - articles
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'title', None, None, ), # 1
    (2, TType.LIST, 'articles', (TType.STRUCT,(Article, Article.thrift_spec)), None, ), # 2
  )

  def __init__(self, title=None, articles=None,):
    self.title = title
    self.articles = articles

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.title = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.articles = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = Article()
            _elem5.read(iprot)
            self.articles.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('News')
    if self.title is not None:
      oprot.writeFieldBegin('title', TType.STRING, 1)
      oprot.writeString(self.title)
      oprot.writeFieldEnd()
    if self.articles is not None:
      oprot.writeFieldBegin('articles', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.articles))
      for iter6 in self.articles:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Message:
  """
  Attributes:
   - title
   - content
   - reason
   - create_time
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'title', None, None, ), # 1
    (2, TType.STRING, 'content', None, None, ), # 2
    (3, TType.STRING, 'reason', None, None, ), # 3
    (4, TType.STRING, 'create_time', None, None, ), # 4
  )

  def __init__(self, title=None, content=None, reason=None, create_time=None,):
    self.title = title
    self.content = content
    self.reason = reason
    self.create_time = create_time

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.title = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.reason = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.create_time = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Message')
    if self.title is not None:
      oprot.writeFieldBegin('title', TType.STRING, 1)
      oprot.writeString(self.title)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 2)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    if self.reason is not None:
      oprot.writeFieldBegin('reason', TType.STRING, 3)
      oprot.writeString(self.reason)
      oprot.writeFieldEnd()
    if self.create_time is not None:
      oprot.writeFieldBegin('create_time', TType.STRING, 4)
      oprot.writeString(self.create_time)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
