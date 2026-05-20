class Solution:
  def licenseKeyFormatting(self, s: str, k: int) -> str:
    chars = s.replace('-', '').upper()
    groups = []

    while chars:
      groups.append(chars[-k:])
      chars = chars[:-k]

    return '-'.join(reversed(groups))