from .. import interface
from typing import Any, Literal, Optional, Union,List
from ..element import Element
from ..element import Element, JSONSerializable
from ..embedded_encoder import ElementJSONEncoder
import json


ARG_MAP={}
def modal(
        content= None,
        title: List[Element]= None,
        visible: bool = None,
        closable: bool = None,
        maskClosable: bool = None,
        width: Union[int, str] = None,
        centered: bool = None,
        footer = None,
        okText: str = None,
        cancelText: str = None,
        onOk = None,
        onCancel= None,
        afterOpenChange= None,
        confirmLoading: bool = None,
        destroyOnClose: bool = None,
        mask: bool = None,
        keyboard: bool = None,
        maskStyle: dict = None,
        style: dict = None,
        wrapClassName: str = None,
        zIndex: int = None,
        okType= None,
        okButtonProps= None,
        modalRender= None,
        getContainer= None,
        focusTriggerAfterClose= None,
        closeIcon= None,
        cancelButtonProps= None,
        bodyStyle= None,
        afterClose= None,
        open= None,
        **kwargs
):
    options = {ARG_MAP.get(key, key): value for key, value in locals().items() if key != 'kwargs' and value is not None}
    options['content'] = str(content)
    #modaltitle = title.as_dict()
    options['title'] = title#json.dumps(modaltitle, default=lambda o: o.__class__.__name__, indent=4)
    options.update(kwargs)
    interface.outbox('openmodal', data=options)