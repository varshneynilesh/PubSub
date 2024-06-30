# gsutil commands
-------------------
$ gsutil notification create -f json -e OBJECT_FINALIZE -t projects/playground-s-11-f98fe0e1/topics/newImage gs://sfoo_images

$ mkdir gen_thumbnail
$ cd gen_thumbnail/

$ gcloud functions deploy gen_thumbnail --runtime python38 --trigger-topic newImage
