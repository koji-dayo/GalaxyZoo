# Galaxy Zoo 1 data release

# Abstract


Projects such as the Galaxy Zoo and The Sloan Digital Sky Survey have made it possible to obtain vast amounts of galaxy data. These galaxies have been morphologically categorized with human visual inspections, but their visual classification take a huge amount of time and not enough reproducity. In this research, we apply machine learning using fea- tures such as central concentration and smoothness of galaxies and deep learning using image data to mor- phological classification of galaxies.

# 研究背景と目的

銀河とは 1,000 億個にも及ぶ多数の星, ガス, チリ, ダークマターなどで構成された天体である. 銀河の形 態には大きさ, 厚み, 構造間の距離など様々な形態が存在する. 有名なもので円盤面に渦状腕と呼ばれる渦巻状のパターンが見られる渦巻銀河銀河や滑らかな楕円形の形状を持つ楕円銀河などが存在する. 銀河の形態学的分類はこうした銀河の形状を分類することである. 銀河の形態を把握することは銀河の誕 生や新たな物理的構成を発見する手がかりとなる. しかし銀河のデータは膨大に存在し人間の目で分類していくには膨大な時間がかかり再現性にかける. 近年ビッグデータを活用した人工知能技術である機械学習と深 層学習が存在する.分類や予測などのタスクを遂行する アルゴリズムやモデルを自動的に構築する技術であり,本研究では銀河の形態学的分類を行うシステムを構築することを目的とする.

# データセット

本研究で用いるデータセットはGalaxyZooに掲載されている分光学赤方偏移を伴うサンプルデータと座標, 測光,サイズ,赤方偏移を含むSDSS Meta Data を用いる.またこれらのカタログを用いてSloan Digital Sky Survey(SDSS) から画像データを入手する.

# GalaxyZoo

GalaxyZooは2007 年に設立された. 大量の銀河のデータを仕分ける必要があり多くの人がそのデータの仕分けに参加できるようにしたオープンサイエンスプ ラットフォームである. 本研究では用いるカタログは分 光学的赤方偏移に基づいた243500 個のカタログであ りそれに基づき赤方偏移や銀河の明るさを測定するときに使われる半径であるペトロシアン半径のデータも 入手した. データの前処理として銀緯が 30 度未満であ ること, 赤方偏移が 0.03 より大きく 0.1 未満であること,銀河のペトロシアン半径の面積を半値全幅の面積で 割ったものが5,10,20 以上であるという条件を設定し銀河を抽出した.

# K

銀河のペトロシアン半径の面積を半値全幅の面積で割ったものである。Kが大きくなるにつれて銀河の個数が少なくなることが判明している。Kを表す式は以下の通りである。

![K](img/k.png,"K")

# The Sloan Digital Sky Survey

The Sloan Digital Sky Surveyとは北米を中心と知った全天の25%の領域で観測し,1億個以上の銀河の位置やスペクトルなどを精密に測定する大規模なプロジェ クトである.本研究では2014年7月にリリースされたSDSS-DR12 カタログを使用する.GalaxyZoo カタ ログから天体座標を入手し, それに基づいて画像を入手する.JPEG 画像を取得するためのWeb APIが公開されており,座標,画像サイズ,解像度などのパラメータを設定することで必要な銀河の画像データを入手する.

# Result

|         | K≥5 | K≥10 | K≥20 |
|---------|-----|------|------|
|accuracy | 97% | 98%  | 98%  |

