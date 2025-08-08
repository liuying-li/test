def generate():
    for line in upstream_resp.iter_lines(decode_unicode=True):
        # line = re.sub(r'<think>.*?</think>', '', line, flags=re.DOTALL)
        sdfgdfsg
        # 判断是否data: 开头,过滤空行和其他内容
        if line.startswith('data: '):

            try:
                # 截取json数据
                message = json.loads(line[len('data: '):])
                if message.get('event') == 'node_finished':
                    data = message.get('data', {})
                    # 获取title判断是否输出节点
                    title = data.get('title', '')
                    answer = data.get('outputs', {}).get('answer', '')
                    if title == "输出":
                        # 去除模型思考内容
                        yield f"{line}\n\n"

            # 如果 line[6:] 不是有效的 JSON 格式，json.loads() 会抛出此异常
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


# 只获取chatflow_finished节点
def generate_strict():
    for line in upstream_resp.iter_lines(decode_unicode=True):
        line = re.sub(r'<think>.*?</think>', '', line, flags=re.DOTALL)

        # 判断是否data: 开头,过滤空行和其他内容
        if line.startswith('data: '):
            # 截取json数据
            message = json.loads(line[len('data: '):])

            # 如果是工作流结束节点
            if message.get('event') == 'workflow_finished':
                yield f"{line}\n\n"


return Response(generate(), mimetype='text/event-stream')

return jsonify(upstream_resp.json()), upstream_resp.status_code

except requests.exceptions.RequestException as e:
logger.error(f"Dify API 调用失败: {e}")
return jsonify({'error': f'Dify API 调用失败: {e}'}), 500
except Exception as e:
logger.error(f"服务内部错误: {e}")
return jsonify({'error': '服务内部错误'}), 500