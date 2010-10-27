.PHONY: tapd

tapd:
	mkdir -p dist/RPMS/x86_64
	mkdir -p src/var/run/tapd/dav
	rpmbuild -bb --target=x86_64 --define "_topdir ${PWD}/dist" --buildroot="${PWD}/src" tapd.spec
	
clean:
	rm -rf dist
	