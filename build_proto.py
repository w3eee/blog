# -*- coding: utf-8 -*-

import os
import glob
import shutil


class Converter(object):

    def __init__(self, proto_dir, output_dir, err_path="lib/errcode"):
        pd_path, pd_name = os.path.split(proto_dir)
        self.source_pd_name = pd_name
        self.pd_name = pd_name
        self.pd_path = pd_path
        self.proto_dir = proto_dir
        self.output_dir = output_dir
        self.err_path = err_path
        if "." in pd_name:
            tp = pd_name.split(".")
            self.pd_name = tp[0]
            self.proto_dir = os.path.join(pd_path, self.pd_name)
            self.errcode_dir = os.path.join(self.proto_dir, err_path)
            # run cp
            try:
                shutil.rmtree(self.proto_dir)
            except:
                pass
            os.chdir(pd_path)
            os.system("cp -r %s %s" % (proto_dir, self.proto_dir))
            # convert protobuf.com to protobuf
            proto_dirs = glob.glob(os.path.join(self.proto_dir, '*/*.proto'))
            proto_dirs.extend(glob.glob(os.path.join(self.errcode_dir, "*.proto")))
            for f in proto_dirs:
                data = open(f, 'r').read()
                data = data.replace(pd_name, self.pd_name)
                open(f, 'w').write(data)
        self.errcode_dir = os.path.join(self.proto_dir, err_path)

    def make_proto(self):
        proto_dirs = glob.glob(os.path.join(self.proto_dir, '*/*.proto'))
        proto_dirs.extend(glob.glob(os.path.join(self.errcode_dir, "*.proto")))
        for d in proto_dirs:
            filename = d.replace(self.pd_path, '.')
            cmd = 'python -m grpc_tools.protoc -I ./  --python_out={output} --grpc_python_out={output} {filename}'.format(
                output=self.output_dir, filename=filename)
            os.chdir(self.pd_path)
            os.system(cmd)
            print('已完成: {}'.format(d))

    def add_init(self):
        dirs_to_add_init = glob.glob(os.path.join(self.output_dir, '{}/*/*.py'.format(self.pd_name)))
        for d in dirs_to_add_init:
            init_file = os.path.join(os.path.split(d)[0], '__init__.py')
            if not os.path.exists(init_file):
                print('添加__init__.py文件: {}'.format(init_file))
                with open(init_file, 'w') as f:
                    f.write('# -*- coding: utf-8 -*-')
        root_init = os.path.join(self.output_dir, self.pd_name, '__init__.py')
        if not os.path.exists(root_init):
            print('添加__init__.py文件: {}'.format(root_init))
            with open(root_init, 'w') as f:
                f.write('# -*- coding: utf-8 -*-')
        errcode_init = os.path.join(self.output_dir,self.pd_name, self.err_path,  "__init__.py")
        if not os.path.exists(errcode_init):
            with open(errcode_init, 'w') as f:
                f.write('# -*- coding: utf-8 -*-')

    def add_header(self):
        files_to_add_header = glob.glob(os.path.join(self.output_dir, '{}/*/*.py'.format(self.pd_name)))
        for file in files_to_add_header:
            with open(file, 'r') as f:
                data = f.read()
                if "coding: utf-8" not in data:
                    data = '{}\n{}'.format('# -*- coding: utf-8 -*-', data)
            with open(file, 'w') as f:
                # print(data)
                f.write(data)

    def run(self):
        self.make_proto()
        self.add_init()
        self.add_header()


def main():
    c = Converter(proto_dir="/data/projects/go/protobuf.com", output_dir="/home/wee/Nproject/UserCoin")
    c.run()


# python -m grpc_tools.protoc -I ./  --python_out=/data/python/ApiGW/ --grpc_python_out=/data/python/ApiGW/
# ./pb/article/article.proto


if __name__ == '__main__':
    main()
