# FastAPI スターターテンプレート

このリポジトリは、FastAPIでバックエンドを構築するためのスターターテンプレートです。（ほぼほぼ自分用ですが）  
データベースやAPIバージョニングに関連するいくつかの機能を予め実装しています。

## ライブラリ

以下は、このスターターテンプレートで使用している主なライブラリです。詳細は`requirements.txt`を参照してください。

- FastAPI: 高速でモダンなWebフレームワーク。[ドキュメント](https://fastapi.tiangolo.com/) [リポジトリ](https://github.com/tiangolo/fastapi)
- SQLModel: FastAPIとの親和性が高い、SQLAlchemyベースのORM。 [ドキュメント](https://sqlmodel.tiangolo.com/) [リポジトリ](https://github.com/tiangolo/sqlmodel)
- Pydantic: FastAPIとSQLModelのベースになっている、堅牢なデータ検証ライブラリ。 [ドキュメント](https://docs.pydantic.dev/latest/) [リポジトリ](https://github.com/pydantic/pydantic)

## ファイル

`alembic.ini`: データベースのマイグレーションに使用する構成ファイルです。  
`crud.py`: データベースのCRUD操作を定義します。  
`database.py`: データベースの接続情報を記載します。接続URIは、`alembic.ini`から自動で参照します。  
`main.py`: メインファイルです。そのまま実行すると、Stat Reloadモードで起動します。  
`models.py`: データベースのモデル（テーブル）を定義します。  
`pagination.py`: APIがページ分けをサポートできるような小さなクラスです。  
`schemas.py`: APIのリクエスト / レスポンススキーマを定義します。  

`migrations/`: Alembicのマイグレーション関連

`api/`: APIをバージョン分けします。  
`api/__init__.py`: APIルーターをバージョン別に登録します。  

`api/v1/`: API バージョン1

`api/v1/__init__.py`: そのバージョンのPythonファイル内にある`router`を自動で`include_router`します。  
`api/v1/main.py`: API バージョン1のメインファイルです。

## 使い方

1. このリポジトリをテンプレートとして、GitHubで新しいリポジトリを作成します。  
または、以下のコマンドでリポジトリをローカルにクローンします。

```sh
git clone https://github.com/ShieruCHR/fastapi-starter-template.git
cd fastapi-starter-template
```

2. 仮想環境を作成・有効化します。

For Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

For macOS / Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

3. 必要なライブラリをインストールします。

```bash
pip install -r requirements.txt
```

4. データベースの設定を行います。  
`alembic.ini`の`[alembic]`セクション内の`sqlalchemy.url`を編集するか、  
`database.py`の`alembic_ini.get("alembic", "sqlalchemy.url")`を任意のURIに置き換えます。

5. `crud.py`, `models.py`, `schemas.py`を編集します。
6. マイグレーションを実行します。

```sh
alembic upgrade head
```

7. アプリケーションを起動します。

```sh
uvicorn main:app --reload
# or "python main.py"
```

## API ドキュメント

FastAPIは、既定でSwagger UIを提供しています。<http://localhost:8000/docs> にアクセスしてください。  
またこのテンプレートでは、アプリケーションの起動時に`openapi.json`を生成します。  
[OpenAPI Generator CLI](https://github.com/OpenAPITools/openapi-generator-cli)などのツールを使用して、簡易的なAPI クライアントを生成できます。

## API バージョニング

このテンプレートには、APIバージョニングを簡単に行うための方法を提供しています。  
新しいバージョンのAPI (`v2`)を作成してみましょう。

1. `api/v1/`を`api/v2/`にコピーする。
2. `api/v2/__init__.py`の`API_VERSION = 1`を`API_VERSION = 2`に変更する。
3. `api/__init__.py`の`api_router`に`v2`のrouterをincludeする。

```diff
from glob import glob
from fastapi import APIRouter

from .v1 import router as v1_router
+ from .v2 import router as v2_router

api_router = APIRouter(prefix="/api")

# Register API Routers
api_router.include_router(v1_router)
+ api_router.include_router(v2_router)
```
