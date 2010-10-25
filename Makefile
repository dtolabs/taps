.PHONY: tapsd

tapsd:
	mkdir -p dist/RPMS/x86_64
	rpmbuild -bb --target=x86_64 --define "_topdir ${PWD}/dist" --buildroot="${PWD}/src" tapd.spec
	
clean:
	rm -rf dist
	