from .. import interface
from typing import Any, Literal, Optional, Union


ARG_MAP = {}
def drawer(
        content: Any,*,
        placement: Literal[
               'top' , 'right' , 'bottom' , 'left'
           ] = 'left',
            size: Optional[Literal[
               'default',
               'large',
             
           ]] = 'default',
           autoFocus = None,
           afterOpenChange = None,
           bodyStyle = None,
           className = None,
           closeIcon = None,
           contentWrapperStyle = None,
           destroyOnClose = None,
           extra = None,
           footer = None,
           footerStyle = None,
           forceRender = None,
           getContainer = None,
           headerStyle = None,
           height = None,
           keyboard = None,
           mask = None,
           maskClosable = None,
           maskStyle = None,
           push = None,
           rootStyle = None,
           style = None,
           title = None,
           open = None,
           width = None,
           zIndex = None,
           onClose = None,
           **kwargs: Any,
        ) -> None:
    
    options = {ARG_MAP.get(key, key): value for key, value in locals().items() if key != 'kwargs' and value is not None}
    options['content'] = str(content)
    options.update(kwargs)
    interface.outbox('opendrawer', data=options)


