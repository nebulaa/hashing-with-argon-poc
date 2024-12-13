# hashing-with-argon-poc

## Description

Simple proof of concept for pasword hashing with Argon2 using argon2-cffi library.

OWASP recommends using Argon2 for password storage.

## Usage

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
To create and store an argon2 hash locally:
```bash
python3 hashing.py
```
To verify an argon2 hash using the local store:
```bash
python3 verify.py
```

## References

Link to the argon2-cffi python library: https://github.com/hynek/argon2-cffi/

Link to OWASP 'Password Storage Cheat Sheet': https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html