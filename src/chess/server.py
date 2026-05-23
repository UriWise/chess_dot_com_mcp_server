from mcp.server.fastmcp import FastMCP

mcp = FastMCP("chess")
from .chess_api import get_player_profile, get_player_stats

@mcp.tool()
def get_chess_player_profile(username: str) -> dict:
    """Fetches the chess player profile from Chess.com API by username."""
    return get_player_profile(username)


@mcp.tool()
def get_chess_player_stats(username: str) -> dict:
    """Fetches the chess player stats from Chess.com API by username."""
    return get_player_stats(username)


def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()