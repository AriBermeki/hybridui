from enum import Enum
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union
from ..element import Element



class Icons(Enum):
    StepBackwardOutlined ='StepBackwardOutlined'
    StepForwardOutlined ='StepForwardOutlined'
    FastBackwardOutlined ='FastBackwardOutlined'
    FastForwardOutlined ='FastForwardOutlined'
    ShrinkOutlined ='ShrinkOutlined'
    ArrowsAltOutlined ='ArrowsAltOutlined'
    DownOutlined ='DownOutlined'
    UpOutlined ='UpOutlined'
    LeftOutlined ='LeftOutlined'
    RightOutlined ='RightOutlined'
    CaretUpOutlined ='CaretUpOutlined'
    CaretDownOutlined ='CaretDownOutlined'
    CaretLeftOutlined ='CaretLeftOutlined'
    CaretRightOutlined ='CaretRightOutlined'
    UpCircleOutlined ='UpCircleOutlined'
    DownCircleOutlined ='DownCircleOutlined'
    LeftCircleOutlined ='LeftCircleOutlined'
    RightCircleOutlined ='RightCircleOutlined'
    DoubleRightOutlined ='DoubleRightOutlined'
    DoubleLeftOutlined ='DoubleLeftOutlined'
    VerticalLeftOutlined ='VerticalLeftOutlined'
    VerticalRightOutlined ='VerticalRightOutlined'
    VerticalAlignTopOutlined ='VerticalAlignTopOutlined'
    VerticalAlignMiddleOutlined ='VerticalAlignMiddleOutlined'
    VerticalAlignBottomOutlined ='VerticalAlignBottomOutlined'
    ForwardOutlined ='ForwardOutlined'
    BackwardOutlined ='BackwardOutlined'
    RollbackOutlined ='RollbackOutlined'
    EnterOutlined ='EnterOutlined'
    RetweetOutlined ='RetweetOutlined'
    SwapOutlined ='SwapOutlined'
    SwapLeftOutlined ='SwapLeftOutlined'
    SwapRightOutlined ='SwapRightOutlined'
    ArrowUpOutlined ='ArrowUpOutlined'
    ArrowDownOutlined ='ArrowDownOutlined'
    ArrowLeftOutlined ='ArrowLeftOutlined'
    ArrowRightOutlined ='ArrowRightOutlined'
    PlayCircleOutlined ='PlayCircleOutlined'
    UpSquareOutlined ='UpSquareOutlined'
    DownSquareOutlined ='DownSquareOutlined'
    LeftSquareOutlined ='LeftSquareOutlined'
    RightSquareOutlined ='RightSquareOutlined'
    LoginOutlined ='LoginOutlined'
    LogoutOutlined ='LogoutOutlined'
    MenuFoldOutlined ='MenuFoldOutlined'
    MenuUnfoldOutlined ='MenuUnfoldOutlined'
    BorderBottomOutlined ='BorderBottomOutlined'
    BorderHorizontalOutlined ='BorderHorizontalOutlined'
    BorderInnerOutlined   ='BorderInnerOutlined'
    BorderOuterOutlined  ='BorderOuterOutlined'
    BorderLeftOutlined  ='BorderLeftOutlined'
    BorderRightOutlined  ='BorderRightOutlined'
    BorderTopOutlined  ='BorderTopOutlined'
    BorderVerticleOutlined ='BorderVerticleOutlined'
    PicCenterOutlined ='PicCenterOutlined'
    PicLeftOutlined  ='PicLeftOutlined'
    PicRightOutlined  ='PicRightOutlined'
    RadiusBottomleftOutlined   ='RadiusBottomleftOutlined'
    RadiusBottomrightOutlined  ='RadiusBottomrightOutlined'
    RadiusUpleftOutlined  ='RadiusUpleftOutlined'
    RadiusUprightOutlined  ='RadiusUprightOutlined'
    FullscreenOutlined  ='FullscreenOutlined'
    FullscreenExitOutlined  ='FullscreenExitOutlined'
    QuestionOutlined='QuestionOutlined'
    QuestionCircleOutlined='QuestionCircleOutlined'
    PlusOutlined='PlusOutlined'
    PlusCircleOutlined='PlusCircleOutlined'
    PauseOutlined='PauseOutlined'
    PauseCircleOutlined='PauseCircleOutlined'
    MinusOutlined='MinusOutlined'
    MinusCircleOutlined='MinusCircleOutlined'
    PlusSquareOutlined='PlusSquareOutlined'
    MinusSquareOutlined='MinusSquareOutlined'
    InfoOutlined='InfoOutlined'
    InfoCircleOutlined='InfoCircleOutlined'
    ExclamationOutlined='ExclamationOutlined'
    ExclamationCircleOutlined='ExclamationCircleOutlined'
    CloseOutlined='CloseOutlined'
    CloseCircleOutlined='CloseCircleOutlined'
    CloseSquareOutlined='CloseSquareOutlined'
    CheckOutlined='CheckOutlined'
    CheckCircleOutlined='CheckCircleOutlined'
    CheckSquareOutlined='CheckSquareOutlined'
    ClockCircleOutlined='ClockCircleOutlined'
    WarningOutlined='WarningOutlined'
    IssuesCloseOutlined='IssuesCloseOutlined'
    StopOutlined='StopOutlined'
    EditOutlined='EditOutlined'
    FormOutlined ='FormOutlined'
    CopyOutlined ='CopyOutlined'
    ScissorOutlined ='ScissorOutlined'
    DeleteOutlined ='DeleteOutlined'
    SnippetsOutlined ='SnippetsOutlined'
    DiffOutlined ='DiffOutlined'
    HighlightOutlined='HighlightOutlined'
    AlignCenterOutlined ='AlignCenterOutlined'
    AlignLeftOutlined ='AlignLeftOutlined'
    AlignRightOutlined ='AlignRightOutlined'
    BgColorsOutlined ='BgColorsOutlined'
    BoldOutlined ='BoldOutlined'
    ItalicOutlined ='ItalicOutlined'
    UnderlineOutlined ='UnderlineOutlined'
    StrikethroughOutlined ='StrikethroughOutlined'
    LineHeightOutlined ='LineHeightOutlined'
    DashOutlined ='DashOutlined'
    SmallDashOutlined ='SmallDashOutlined'
    SortAscendingOutlined ='SortAscendingOutlined'
    SortDescendingOutlined ='SortDescendingOutlined'
    DragOutlined ='DragOutlined'
    OrderedListOutlined ='OrderedListOutlined'
    UnorderedListOutlined ='UnorderedListOutlined'
    RadiusSettingOutlined ='RadiusSettingOutlined'
    ColumnWidthOutlined ='ColumnWidthOutlined'
    ColumnHeightOutlined ='ColumnHeightOutlined'
    AreaChartOutlined='AreaChartOutlined'
    PieChartOutlined='PieChartOutlined'
    BarChartOutlined='BarChartOutlined'
    DotChartOutlined='DotChartOutlined'
    LineChartOutlined='LineChartOutlined'
    RadarChartOutlined='RadarChartOutlined'
    HeatMapOutlined='HeatMapOutlined'
    FallOutlined='FallOutlined'
    RiseOutlined='RiseOutlined'
    StockOutlined='StockOutlined'
    BoxPlotOutlined='BoxPlotOutlined'
    FundOutlined='FundOutlined'
    SlidersOutlined='SlidersOutlined'