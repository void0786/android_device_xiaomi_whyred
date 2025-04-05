#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
 
 import extract_utils.tools
 
 extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_17_2'
 
 from extract_utils.fixups_blob import (
     blob_fixup,
     blob_fixups_user_type,
 )
 from extract_utils.fixups_lib import (
     lib_fixup_remove,
     lib_fixups,
     lib_fixups_user_type,
 )
 from extract_utils.main import (
     ExtractUtils,
     ExtractUtilsModule,
 )
 
 namespace_imports = [
     'device/xiaomi/bouquet-common',
     'hardware/qcom-caf/bouquet',
     'hardware/qcom/wlan/legacy',
     'hardware/xiaomi',
     'vendor/qcom/opensource/dataservices',
 ]
 
 module = ExtractUtilsModule(
     'whyred',
     'xiaomi',
     namespace_imports=namespace_imports,
 )
 
 if __name__ == '__main__':
     utils = ExtractUtils.device(module)
     utils.run()