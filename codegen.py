from ariadne_codegen.main import client
import os

client(
    {
        "ariadne-codegen": dict(
            remote_schema_url=os.environ["MONDAY_API_URL"],
            target_package_path="src",
            target_package_name="mondne",
            enable_custom_operations=True,
            remote_schema_headers={"Authorization": os.environ["MONDAY_API_KEY"]},
            include_comments="none"
        )
    }
)
