LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := myDecompJNI
LOCAL_SRC_FILES := decompJNI.c lz4.c lz4frame.c lz4hc.c xxhash.c

include $(BUILD_SHARED_LIBRARY)