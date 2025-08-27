import streamlit as st
import itertools

def can_make_24(numbers):
    for nums in itertools.permutations(numbers):
        for ops in itertools.product(['+', '-', '*', '/'], repeat=3):
            expressions = [
                f"(({nums[0]}{ops[0]}{nums[1]}){ops[1]}{nums[2]}){ops[2]}{nums[3]}",
                f"({nums[0]}{ops[0]}({nums[1]}{ops[1]}{nums[2]})){ops[2]}{nums[3]}",
                f"{nums[0]}{ops[0]}(({nums[1]}{ops[1]}{nums[2]}){ops[2]}{nums[3]})",
                f"{nums[0]}{ops[0]}({nums[1]}{ops[1]}({nums[2]}{ops[2]}{nums[3]}))",
                f"({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]})"
            ]
            for expr in expressions:
                try:
                    if abs(eval(expr) - 24) < 1e-6:
                        return True, expr
                except ZeroDivisionError:
                    continue
    return False, None

st.title("เกม 24")
numbers_input = st.text_input("กรอกตัวเลข 4 ตัว (คั่นด้วยช่องว่าง):")

if numbers_input:
    try:
        numbers = list(map(int, numbers_input.strip().split()))
        if len(numbers) != 4:
            st.error("กรุณากรอกตัวเลขให้ครบ 4 ตัว")
        else:
            result, expression = can_make_24(numbers)
            if result:
                st.success(f"สามารถสร้าง 24 ได้โดยใช้: {expression}")
            else:
                st.warning("ไม่สามารถสร้าง 24 ได้จากตัวเลขที่ให้มา")
    except ValueError:
        st.error("กรุณากรอกเฉพาะตัวเลขเท่านั้น")
