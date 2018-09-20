Sanhe's Note for Learning Bokeh
==============================================================================

因为工作需要, 想要构建一个Dashboard作为Monitor面板. 当时考虑了 AWS QuickSight, Tabulea 等商业方案, 觉得虽然工作中最终大概率选择商业方案. 可是为了自己学习的缘故, 学习一个开源的解决方案是很有必要的.

- Q: Bokeh是什么?
- A: Bokeh是一个数据可视化的工具, 主要用来创建Web端, 可交互的图表.

- Q: Bokeh可以用来干什么?
- A: 快速的实现一个原型, 并向他人展示, 分享. 并且可以做成一个网站部署到云上, 可以做成一个Dashboard.

- Q: Bokeh不适合用来干什么?
- A: 作为产品端的数据可视化. 产品端的数据可视化目前还是D3.js的天下. 功能还是D3.js强.


header2
------------------------------------------------------------------------------



Interaction (互动)
------------------------------------------------------------------------------



- `Interactive Legends <https://bokeh.pydata.org/en/latest/docs/user_guide/interaction/legends.html#>`_
    - `Hiding Glyphs <https://bokeh.pydata.org/en/latest/docs/user_guide/interaction/legends.html#hiding-glyphs>`_: 隐藏
    - `Muting Glyphs <https://bokeh.pydata.org/en/latest/docs/user_guide/interaction/legends.html#muting-glyphs>`_: 淡化
-